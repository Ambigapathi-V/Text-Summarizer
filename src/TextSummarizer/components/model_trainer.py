from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
import torch
from src.TextSummarizer.logging import logger
from datasets import load_from_disk
from src.TextSummarizer.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        logger.info("ModelTrainer initialized with configuration: %s", self.config)

    def train(self):
        # Setting up the device
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        logger.info("Using device: %s", device)

        # Loading the tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        logger.info("Model and tokenizer loaded from checkpoint: %s", self.config.model_ckpt)

        # Setting up data collator
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        logger.info("Data collator initialized.")

        # Loading the dataset
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        logger.info("Dataset loaded from path: %s", self.config.data_path)

        # Training arguments
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs or 1,
            warmup_steps=self.config.warmup_steps or 500,
            per_device_train_batch_size=self.config.train_batch_size or 1,
            per_device_eval_batch_size=self.config.eval_batch_size or 1,
            weight_decay=self.config.weight_decay or 0.01,
            logging_steps=self.config.logging_steps or 10,
            evaluation_strategy='steps',
            eval_steps=self.config.eval_steps or 500,
            save_strategy='epoch',
            gradient_accumulation_steps=self.config.gradient_accumulation_steps or 16
        )
        logger.info("Training arguments set up with: %s", trainer_args)

        # Initialize Trainer
        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["train"],
            eval_dataset=dataset_samsum_pt["validation"]
        )
        logger.info("Trainer initialized.")

        # Start training
        logger.info("Starting training...")
        trainer.train()
        logger.info("Training complete.")

        # Save the model and tokenizer
        model_save_path = os.path.join(self.config.root_dir, "pegasus-samsum-model")
        tokenizer_save_path = os.path.join(self.config.root_dir, "tokenizer")
        
        model_pegasus.save_pretrained(model_save_path)
        tokenizer.save_pretrained(tokenizer_save_path)
        
        logger.info("Model saved to %s", model_save_path)
        logger.info("Tokenizer saved to %s", tokenizer_save_path)