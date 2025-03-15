from app import app, db
from bot.bot_perfumes import start_bot

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    start_bot()