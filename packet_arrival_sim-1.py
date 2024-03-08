import numpy as np

class Packet:
    def __init__(self, arrival_time):
        """Initialize a packet with its arrival time."""
        self.arrival_time = arrival_time
        # Optional: Add more attributes here if needed for advanced processing

class Router:
    def __init__(self, processing_rate, max_buffer_size):
        """Initialize the router with given processing rate and buffer size."""
        self.processing_rate = processing_rate
        self.max_buffer_size = max_buffer_size
        self.queue = []  # Queue to hold packets
        self.dropped_packets = 0  # Counter for dropped packets
        self.total_packets = 0  # Counter for total packets arrived
    
    def process_packet(self, packet):
        """Process an incoming packet. Implement AQM logic here."""
        
        # AQM/RED Algorithm Placeholder: Implement your logic to decide whether to drop or enqueue the packet
        ##########################
        # IMPLEMENT AQM LOGIC HERE
        ##########################
        
        if len(self.queue) >= self.max_buffer_size:
            self.dropped_packets += 1
            return False  # Drop packet due to buffer overflow
        else:
            self.queue.append(packet)  # Accept and enqueue the packet
            return True

    def simulate_arrivals(self, lambda_rate, duration):
        """Simulate packet arrivals at the router over a specified duration."""
        current_time = 0
        while current_time < duration:
            # Generate next packet arrival using exponential distribution
            interarrival_time = np.random.exponential(1/lambda_rate)
            current_time += interarrival_time
            packet = Packet(current_time)
            
            self.total_packets += 1
            self.process_packet(packet)

# Simulation parameters
lambda_rate = 100  # Average packets per second
duration = 10  # Simulation time in seconds
processing_rate = 100  # Packets per second, adjust as needed
max_buffer_size = 1000  # Maximum packets the buffer can hold

# Initialize router and run simulation
router = Router(processing_rate, max_buffer_size)
router.simulate_arrivals(lambda_rate, duration)

# Output simulation results
print(f"Total packets: {router.total_packets}")
print(f"Dropped packets: {router.dropped_packets}")
print(f"Drop rate: {router.dropped_packets / router.total_packets:.2%}")
