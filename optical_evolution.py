import time

def simulate_optical_link(technology, data_rate_gbps, latency_ms, power_consumption_watts):
    """Simulates a basic optical link technology with its characteristics."""
    print(f"\n--- Simulating {technology} --- ")
    print(f"  Data Rate: {data_rate_gbps} Gbps")
    print(f"  Latency: {latency_ms} ms")
    print(f"  Power Consumption: {power_consumption_watts} W")
    # Simulate data transfer process
    print("  Initiating data transfer...")
    time.sleep(0.1) # Simulate transmission time
    print("  Data transfer complete.")

def main():
    """Demonstrates the evolution from MPO to NPO to CPO."""
    print("Simulating the evolution of optical interconnect technologies.")

    # MPO (Multi-fiber Push On) - Represents older, simpler fiber connectivity
    # Lower data rates, higher latency, moderate power consumption
    simulate_optical_link("MPO", 400, 5.0, 15.0)

    # NPO (Next-gen Parallel Optics) - Represents advancements in parallel optics
    # Higher data rates, lower latency, improved power efficiency
    simulate_optical_link("NPO", 800, 3.0, 12.0)

    # CPO (Co-Packaged Optics) - Represents the latest trend of integrating optics with compute
    # Significantly higher data rates, ultra-low latency, optimized power consumption
    simulate_optical_link("CPO", 1600, 1.0, 8.0)

    print("\nEvolutionary trend shows increased speed, reduced latency, and better power efficiency.")

if __name__ == "__main__":
    main()
