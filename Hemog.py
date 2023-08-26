class HemogramAnalyzer:
    def __init__(self):
        self.normal_ranges = {
            'hemoglobin': (13.5, 17.5),  # g/dL
            'white_blood_cells': (4000, 11000),  # cells/mm³
            'platelets': (150000, 450000),  # cells/mm³
            'red_blood_cells': (4.5, 5.5),  # million/mm³
            'hematocrit': (38, 50),  # %
        }

    def analyze_hemogram(self, results):
        analysis = {}

        for parameter, value in results.items():
            if parameter in self.normal_ranges:
                normal_range = self.normal_ranges[parameter]
                if value < normal_range[0]:
                    analysis[parameter] = "Below normal range"
                elif value > normal_range[1]:
                    analysis[parameter] = "Above normal range"
                else:
                    analysis[parameter] = "Within normal range"
            else:
                analysis[parameter] = "Parameter not recognized"

        return analysis


# Example hemogram results
hemogram_results = {
    'hemoglobin': 15.2,
    'white_blood_cells': 8000,
    'platelets': 250000,
    'red_blood_cells': 5.0,
    'hematocrit': 45,
}

analyzer = HemogramAnalyzer()
result_analysis = analyzer.analyze_hemogram(hemogram_results)

for parameter, analysis in result_analysis.items():
    print(f"{parameter}: {analysis}")
