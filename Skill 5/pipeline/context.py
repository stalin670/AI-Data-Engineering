class PipelineContext:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.features = None
        self.prediction = None
        self.output_record = None
