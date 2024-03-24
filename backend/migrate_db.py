from session_factory import get_my_session, engine
from modules.tables import Base
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)