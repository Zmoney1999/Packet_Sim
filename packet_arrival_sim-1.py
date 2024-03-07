import random
import time
import queue


def simulate_packet(lambda_value , simulation_time , buffer_capacity , packet_buffer):

    current_time = 0 #Average rate (packets per second)
    packet_count = 0 # Total simulation time
    lost_packets = 0

    while current_time < simulation_time:
        # Generate time until next packet arrival
        next_arrival = random.expovariate(lambda_value)

        #Update the current time with them time until the next arrival
        current_time += next_arrival

        if current_time < simulation_time:
            packet_count +=1 # Increase the packet count 
            #INFO: Buffer is full so that packet is lost
            #TODO: We can implement AQM algorithims here
            if packet_buffer.full():
                #TEST simulate a buffer overflow
                print("BUFFER OVERFLOW")
                # The packet is lost when the buffer is full
                lost_packets +=1
                print(f"Packet {packet_count} arrived at time {current_time:.2f}s")
            #Process the packet if the buffer isnt full
            else:
                packet_buffer.put(packet_count)
                print(f"Packet {packet_count} arrived and buffered at time {current_time:.2f}s")
    print(f"Simulation finished. {packet_count} packets arrived over {simulation_time} seconds.")

    return lost_packets

    
def main():

#Program Start

    lambda_value = 1 # Arrival Rate
    simulation_time = 10 #MAX simulation time
    buffer_capacity = 5 #MAX buffer capacity
    packet_buffer = queue.Queue(maxsize=buffer_capacity)
    #This function will simulate packet arriving at a router
    lost_packets = simulate_packet(lambda_value , simulation_time , buffer_capacity , packet_buffer)


    #TEST see which packets were processed
    while not packet_buffer.empty():
        packet_number = packet_buffer.get()
        print("Packet #: " , packet_number , " was processed")

    print("\n # of packets lost" ,lost_packets)
#Program End
if __name__ == "__main__":
    main()
