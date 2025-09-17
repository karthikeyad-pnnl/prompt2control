import DyMat
import os

class MatToTextExporter:
    def __init__(self, mat_path, output_txt_path,time_step = 10):
        self.mat_path = mat_path
        self.output_txt_path = output_txt_path
        self.reader = None
        self.names = []
        self.time_step = time_step
    def load(self):
        self.reader = DyMat.DyMatFile(self.mat_path)
        self.names = self.reader.names()

    def export_summary(self):
        self.load()
        with open(self.output_txt_path, "w") as f:
            f.write(f"This is the simulation result of the first {str(self.time_step)} time points for each variable:\n\n")

            for var in self.names:
                try:
                    time = self.reader.abscissa(var, 0)[0][:self.time_step]
                    values = self.reader.data(var)[:self.time_step]
                    f.write(f"{var}:\n")
                    for t, v in zip(time, values):
                        f.write(f"  t={t:.2f}, value={v:.4g}\n")
                    f.write("\n")
                except Exception:
                    # Skip variables that don’t have a time series or are malformed
                    continue

        print(f"✅ Export completed: {self.output_txt_path}")

if __name__ == "__main__":
    mat_path = "Buildings.Controls.OBC.CDL.Examples.Task2_res.mat"
    output_path = "simulation_results.txt"
    exporter = MatToTextExporter(mat_path, output_path)
    exporter.export_summary()


