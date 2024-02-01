from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine=create_engine('postgresql://postgres:root@localhost/food_main_delivered',
    echo=True
)

Base=declarative_base()

Session=sessionmaker()