from src.data.ingest import load_data

def test_data_loading():
    df = load_data("data/raw/printer_data.csv")
    assert df.shape[0] > 0
