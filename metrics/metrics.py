"""
metrics.py

This module is responsible for collecting and reporting
pipeline metrics.

Metrics answer the question:
"How did the pipeline behave?"

NOT:
"What data was processed?"
"""

# -------------------------
# Metrics class definition
# -------------------------

class PipelineMetrics:
    """
    PipelineMetrics stores counters related to pipeline execution.

    This class is NOT responsible for:
    - validation
    - ingestion
    - storage

    It only counts and reports numbers.
    """

    def __init__(self):
        """
        Constructor method.
        This runs automatically when we create an object of this class.

        All counters are initialized to zero.
        """

        # Total records seen by the pipeline (CSV + JSON)
        self.total_records = 0

        # Records that passed validation
        self.valid_records = 0

        # Records that failed validation
        self.rejected_records = 0

        # Records coming specifically from CSV source
        self.csv_records = 0

        # Records coming specifically from JSON source
        self.json_records = 0

    # -------------------------
    # Increment methods
    # -------------------------

    def increment_total(self):
        """
        Increases total record count by 1.

        Called every time a record is read,
        regardless of valid or rejected.
        """
        self.total_records += 1

    def increment_valid(self):
        """
        Increases valid record count by 1.

        Called only when a record passes validation.
        """
        self.valid_records += 1

    def increment_rejected(self):
        """
        Increases rejected record count by 1.

        Called only when validation fails.
        """
        self.rejected_records += 1

    def increment_csv(self):
        """
        Increases CSV record count by 1.

        Called when a record is read from CSV source.
        """
        self.csv_records += 1

    def increment_json(self):
        """
        Increases JSON record count by 1.

        Called when a record is read from JSON source.
        """
        self.json_records += 1

    # -------------------------
    # Reporting method
    # -------------------------

    def summary(self):
        """
        Returns a dictionary containing all metric values.

        This method does NOT print.
        Printing/logging is responsibility of main.py.
        """

        return {
            "total_records": self.total_records,
            "valid_records": self.valid_records,
            "rejected_records": self.rejected_records,
            "csv_records": self.csv_records,
            "json_records": self.json_records,
        }
