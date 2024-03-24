from flask_factory import get_session_engine
from modules.tables import Base
_, engine = get_session_engine()
Base.metadata.create_all(bind=engine)