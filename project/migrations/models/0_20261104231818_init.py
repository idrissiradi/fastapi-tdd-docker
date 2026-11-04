from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "textsummary" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "url" TEXT NOT NULL,
    "summary" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztll1vmzAUhv8K4qqVtqrN0g/tjqXZmqkhVYO2qtNkOeAQFGNTY9ZEXf77fAzEhBDU7m"
    "JTo97Be17bx4/xOTzZMQ8ITY88spDjLI6xWNofrSeb4Zioh6bwO8vGSWKCIEg8odovlTGt"
    "GCepFNiXKjTFNCVKCkjqiyiREWdKZRmlIHJfGSMWGilj0UNGkOQhkTMiVODHTyVHLCALkp"
    "avyRxNI0KDjaSjANbWOpLLRGsDJj9rI6w2QT6nWcyMOVnKGWdrd8QkqCFhRGBJYHopMkgf"
    "sis2W+4oz9RY8hQrYwIyxRmVle1OkNFshNyRh8Z9DyH7BYB8zgCuSjXVuw8hhfedk+559+"
    "LDWfdCWXSaa+V8lS9twOQDNR7Xs1c6jiXOHZqxgZoJuk0VvotmrIW9xlUlXOdaUmwDWwqG"
    "rPma/gHaFm5e/86DmeM0faAguN+c296Vc3swdO4OdWRZRK5H7pfSztWlyC+M27sefdLoDe"
    "rKBXou7sqQN+R/gdwXBOAgLLepX6qIjGLSTH5zZA1+UAw9Kh9e4VHYaoPBiNFlUdDajmYw"
    "7I89Z3izcT6XjteHSGfjbEr14Oxw83jWk1jfB96VBa/W/cjta7w8laHQKxqfd29DTjiTHD"
    "H+iHBQqb2lWlJbQdeYzislDoQJ9uePWARoK8I7fJd3OxR34rqCGQ71mQFcSLPoqA4RkT9r"
    "6rVFpLXNYuN567D70mF/EZFCSltkezMsmtFWhuxF2Vf3ZYEoYaGEq9E5PW0BWlZ95apVkL"
    "IhdPLYZqWHS/UCwoV9D+meHB8/g65y7aSrY7U+ypkkrKGJfh2P3B0N1Aypd8/Il9Zvi0bp"
    "Vq14BbRb4AKM9l+Y+t9KrffBBPAL81+b2eoPOD6HmQ=="
)
