# All movies info were taken from IMDb website
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Genre, Item, User
import datetime

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

User1 = User(name="Rawan Hamad", email="rawaneeta1@gmail.com",
             picture='https://pbs.twimg.com/profile_images/'
             '2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


# genres
Genre1 = Genre(user_id=1, name="Action")
session.add(Genre1)
session.commit()


Genre_item_1_1 = Item(title="The Equalizer",
                      description='A man believes he has put his mysterious'
                      'past behind him and has dedicated himself to '
                      'beginning a new, quiet life. But when he meets'
                      ' a young girl under the control of ultra-violent'
                      ' Russian gangsters, he can\'t '
                      'stand idly by - he has to help her',
                      user_id=1,
                      genre=Genre1)

session.add(Genre_item_1_1)
session.commit()


Genre_item_1_2 = Item(title="Mad Max: Fury Road",
                      description='In a post-apocalyptic wasteland, '
                      'a woman rebels against a tyrannical ruler in search '
                      'for her homeland with the aid of a group of female '
                      'prisoners, a psychotic worshiper,'
                      'and a drifter named Max.',
                      user_id=1,
                      genre=Genre1)

session.add(Genre_item_1_2)
session.commit()


Genre2 = Genre(user_id=1, name="Adventure")
session.add(Genre2)
session.commit()

Genre_item_2_1 = Item(title="Gladiator",
                      description='A former Roman General sets out to exact'
                      ' vengeance against the corrupt emperor who murdered '
                      'his family and sent him into slavery.',
                      user_id=1,
                      genre=Genre2)

session.add(Genre_item_2_1)
session.commit()


Genre_item_2_2 = Item(title="Inception",
                      description='A thief who steals corporate secrets'
                      'through the use of dream-sharing technology is'
                      ' given the inverse task of planting an idea into'
                      ' the mind of a CEO.',
                      user_id=1,
                      genre=Genre2)

session.add(Genre_item_2_2)
session.commit()


Genre3 = Genre(user_id=1, name="Comedy")
session.add(Genre3)
session.commit()

Genre_item_3_1 = Item(title="Step Brothers",
                      description='Two aimless middle-aged losers still living'
                      ' at home are forced against their will to become '
                      'roommates when their parents marry.',
                      user_id=1,
                      genre=Genre3)

session.add(Genre_item_3_1)
session.commit()


Genre4 = Genre(user_id=1, name="Drama")
session.add(Genre4)
session.commit()

Genre_item_4_1 = Item(title="The Godfather",
                      description='The aging patriarch of an organized crime'
                      ' dynasty transfers control of his clandestine empire'
                      'to his reluctant son.',
                      user_id=1,
                      genre=Genre4)

session.add(Genre_item_4_1)
session.commit()


Genre5 = Genre(user_id=1, name="Horror")
session.add(Genre5)
session.commit()

Genre_item_5_1 = Item(title="The Wailing",
                      description='Soon after a stranger arrives in a little'
                      'village, a mysterious sickness starts spreading.'
                      'A policeman, drawn into the incident, is forced to'
                      'solve the mystery in order to save his daughter.',
                      user_id=1,
                      genre=Genre5)

session.add(Genre_item_5_1)
session.commit()

Genre6 = Genre(user_id=1, name="Sci-fi")
session.add(Genre6)
session.commit()

Genre_item_6_1 = Item(title=" Westworld",
                      description='Set at the intersection of the near future'
                      'and the reimagined past, explore a world in which every'
                      ' human appetite can be indulged without consequence.',
                      user_id=1,
                      genre=Genre6)

session.add(Genre_item_6_1)
session.commit()

print "added catalog items!"
