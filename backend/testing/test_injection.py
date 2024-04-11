from testing_setup import FlaskTests
import pytest
from io import BytesIO
from uuid import UUID, uuid4
import time
class Test_Analyser(FlaskTests):

    def test_user_uploading(self):