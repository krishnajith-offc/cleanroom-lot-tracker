import datetime
import random
import time


class WaferLot:

    def __init__(self, lot_id, product_type, total_wafers=25):
        self.lot_id = lot_id
        self.product_type = product_type
        self.total_wafers = total_wafers
        self.status = "Created"
        self.history = []

    def log_step(self, process_name, operator):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = f"[{timestamp}] Process: {process_name} | Operator: {operator} | Status: OK"
        self.history.append(record)
        self.status = f"Completed {process_name}"
        print(record)

    def run_quality_inspection(self):
        defects = random.randint(0, 2)
        passed_wafers = self.total_wafers - defects
        print(
            f"--> Quality Check for {self.lot_id}: {passed_wafers}/{self.total_wafers} Passed ({defects} Defects Detected)"
        )
        return defects


def main():
    print("=== INFINEON CLEANROOM LOT TRACKING SYSTEM (SIMULATION) ===")
    print("Initializing Line Operations...\n")

    # Creating Sample Wafer Lots
    lot_1 = WaferLot(
        lot_id="LOT-INF-2026-001", product_type="Power Semiconductor"
    )

    # Simulating Shift Operations
    lot_1.log_step(
        process_name="Silicon Wafer Loading", operator="Krishnajith"
    )
    time.sleep(1)

    lot_1.log_step(process_name="LPCVD Thin Film Deposition", operator="Shift-A")
    time.sleep(1)

    lot_1.run_quality_inspection()

    lot_1.log_step(
        process_name="Automated Packaging & Transport", operator="Shift-A"
    )

    print("\n=== LOT HISTORY LOG ===")
    for log in lot_1.history:
        print(log)


if __name__ == "__main__":
    main()
