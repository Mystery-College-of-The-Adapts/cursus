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

*at 1 byte of data per operation, Bandwidth = 10 ^ 8 bytes / s*


**Example3**

*What is the Bandwidth of a memory system that has a Latency of 20 ns, a precharge time of 5 ns, and transfers 2 bytes per data per access?*

**Solution**

*The Latency of 20 ns and precharge time of 5 ns combine to allow a new memory reference to be started every 25 ns.*

*Throughput = 1 / 25 ns = 4 x 10 ^ 7 operations/s*


_________________________________________________________________________________________
## Memory Hierarchies

- The primary reason that memory systems are constructed as Hierarchies is that the cost per bit of a memory technology is generally proportional to the speed of the technology.
- Fast memories, such as static RAMs(SRAM) tend to have a high cost per bit (in both dollars and chip area).
- Slower technologies, such as dynamic RAM(DRAM) are less expensive, making it practical to construct larger memories using these technologies.

**1. Why are computers' memory systems typically built as Hierarchies?**
*Solution*

- The faster a memory technology is, the more it tends to cost per bit of storage. 
- Using a memory hierarchy allows the computer to provide a large memory capacity, fast average access time, and low memory cost.
- The lower levels of the memory hierarchy, which contain the most storage, are implemented using slow but cheap memory technologies.
- The higher levels,  which contain smaller amounts of storage, are implemented in fast but expensive memory technologies.
- As data is referenced, it is moved into the higher levels of the memory hierarchy so that most memory references are handled by the top levels of the hierarchy.
- If enough references are handled by the top levels of the hierarchy, the memory system gives an average access time similar to that of the fastest level of the hierarchy, with a cost per bit similar to that of the fastest level of the hierarchy, with a cost per bit similar to that of the lowest level of hierarchy.


**2. Suppose that SRAM costs $25 per MB for an access time of 5 ns, DRAM costs $1 per MB with an access time of 60ns, and disk space costs $10 per 1GB with an access time of 7 ms.**

- **For a memory system with 256KB of cache SRAM, 128MB of main memory DRAM, and 1 GB of virtual memory(implemented as disk), what is the total cost of the memory system and the cost per byte?**
- **If the hit rate at each level in the memory hierarchy is 80 % (except the last), what is the average memory access time?**
- **What is the average memory access time if the hit rate at each level except the last is 90%?**
- **How about if the hit rate is 99% at each level except the last?**

*Solution*

- Costs
    - SRAM costs $25 per MB, so 256KB (1/4 MB) of SRAM cost = 1/4 x 25 = $6.25
    - 128MB of DRAM cost = 128 x 1 = $128
    - 1GB of disk space cost = 1 x 10 = $10
    - Total Cost = 6.25 + 128 + 10 = $144.25
    - To get the cost per byte, we divided by the total storage of 256KB + 128MB + 1GB = 1,208,221,696 Bytes, so the toal cost per byte = $1.19 x 10 ^ -7 per Byte
    
- For each level, average access time = (hit rate x access time for that level) + ( 1 - hit rate) x (average access time for next level)
    - Therefore the access time = (0.80 x 5ns) + 0.20 x (0.80 x 60ns) + 0.20 x 7ms = 280,013.6ns
    
- Changing the hit rates from the above equation, we get an average access time of 70,009.9 ns

- With these hit rates, the average access time is 705.5 ns



**3. In a two-level memory Hierarchy, if the top level has an access time of 8ns and the bottom level has an access time of 60 ns, what is the hit rate in the top level required to give an average access time of 10 ns?**

*Solution*

By using the formula for average access time in a memory

average access time = (hit rate x access time for that level) + ( 1 - hit rate) x (average access time for next level)

10ns = (hit rate x 8ns ( 1 - hit rate) x (60ns)

**hit rate** = 96.2%


______________________________________________________________________________________________

## Inclusion

**1. Explain why maintaining inclusion between different levels of the memory hierarchy makes implementing write-back memory hierarchies easier**

*Solution*

- Maintaining inclusion between levels in the memory hierarchy (ensuring that all data in a level is also contained in all of the levels below it) makes it easier to implement write-back memory hierarchies because it guarantees that, when a block of data is removed from a level of the hierarchy, there is space on the next lower level to write data if it has been modified.

- If the levels of a hierarchy did not maintain inclusion, then there might not be space in the next lower level to write the block, requiring that a block be removed from that level to make space, which would make removing blocks more complicated.


