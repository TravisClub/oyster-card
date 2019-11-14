from unittest.mock import patch, mock_open
from unittest.mock import MagicMock
from oyster.oyster_card import *
import pytest


# def test_read_stations_file_reads_json_file():
#     file_content_mock = {"stations": [{"name": "Alvaro", "zone": [1]}]}
#     fake_file_path = 'file/path/mock.json'
#     with patch('oyster.oyster_card.open'.format(__name__),
#                new=mock_open(read_data=file_content_mock)) as _file:
#         actual = read_stations_file(fake_file_path)
#         _file.assert_called_once_with(fake_file_path, 'r')
#     expected = {"stations": [{"name": "Alvaro", "zone": [1]}]}
#     assert actual == expected


def test_read_stations_file_swallows_filenotfounderror_exception_when_non_existing_directory_indicated():
    with pytest.raises(FileNotFoundError) as ke:
        read_stations_file('fakeFile.json')
        assert "No such file or directory" in str(ke.value)

