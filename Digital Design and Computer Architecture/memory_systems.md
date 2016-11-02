## Latency, Throughput, and Bandwidth

- **Latency** is time taken to complete an individual operation
- **Throughput** is the rate at which operations can be completed
- **Bandwidth** is the total rate at which data can be moved between the processor and the memory system.

    i.e Bandwidth = Throughput * amount of data referenced by each memory operation.


**Example1**

*If a memory system has a Latency 10ns per operation and a data width of 32 bits, what is the Throughput and Bandwidth of the memory system,
assuming only one operation can be performed at a time and there is no delay between operations?*


**Solution**

*Throughput = 1 / Latency   when operations execute sequentially*

*Throughput = 1 / 10 ns = 100 million operations per second*

*Each operation references 32 bits of data*

*The Bandwidth is 3.2 billion bits/s or 400 million bytes/s*


- Memory systems can be pipelined in the same way that processors are pipelined.
- Many memory technologies require that a certain amount of idle time elapse between memory accesses.
- This time is used to **prepare** or **precharge**, the circuitry for the next access.

**Example2**

*What is the Bandwidth of a memory system with a Latency of 40 ns, that transfers 1 byte per operation, and is pipelined to allow 4 operations 
to overlap execution(assume no execution overhead)?*

**Solution**

*Throughput = 4 operations / 40 ns = 1 operation per 10 ns*

*at 1 byte of data per operation, Bandwidth = 10 ^ 8 bytes / s *


**Example3**

*What is the Bandwidth of a memory system that has a Latency of 20 ns, a precharge time of 5 ns, and transfers 2 bytes per data per access?*

**Solution**

*The Latency of 20 ns and precharge time of 5 ns combine to allow a new memory reference to be started every 25 ns.*

*Throughput = 1 / 25 ns = 4 x 10 ^ 7 operations/s *