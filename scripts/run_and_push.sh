#!/bin/bash

LOG_FILE="run_log.txt"
exec > >(tee -a "$LOG_FILE") 2>&1

echo "🚀 Starting StudentPerformanceML pipeline..."

echo "🔄 Running preprocess.py..."
python3 preprocess.py

echo "🔄 Running train_model.py..."
python3 train_model.py

echo "🔄 Running evaluate.py..."
python3 evaluate.py

echo "📁 Adding changes to Git..."
git add .

echo "📝 Committing changes..."
git commit -m "Automated commit from run_and_push.sh"

echo "🔄 Pulling latest from GitHub..."
git pull origin main --rebase

echo "🚀 Pushing to GitHub..."
git push origin main

echo "✅ All done! Log saved to $LOG_FILE"

