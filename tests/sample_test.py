from nyc_taxi_eta.components.data_ingestion import (
    DataIngestion,
)


def test_data_ingestion():
    # Create an instance of DataIngestion
    data_ingestion = DataIngestion(file_paths=["sample.parquet"])

    assert data_ingestion is not None, (
        "DataIngestion instance should be created successfully"
    )
