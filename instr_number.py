import re

def extract_cpi(report):

    exec_blocks = re.findall(r"EXEC NAME: (.+?)\n.*?Real instructions: (\d+)", report, re.DOTALL)

    for exec_name,  instructions in exec_blocks:

        instructions = int(instructions)


      


        print(f"{exec_name}: instr number = {instructions}")


report_data = """

EXEC NAME: aha-mont64
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 8684328
Real instructions: 4531262
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/aha-mont64.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/aha-mont64.irom8.hex
Simulation fast clock cycles (/1): 17410928
Simulation main clock cycles (/2): 8705464

------------------------------
           HART: 0
------------------------------
Cycles: 8705459
Time: 8705459
Retired instructions: 4542231
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: crc32
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 6794323
Real instructions: 3831160
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/crc32.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/crc32.irom8.hex
Simulation fast clock cycles (/1): 13669594
Simulation main clock cycles (/2): 6834797

------------------------------
           HART: 0
------------------------------
Cycles: 6834792
Time: 6834792
Retired instructions: 3853897
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: cubic
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 12567004
Real instructions: 5803827
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/cubic.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/cubic.irom8.hex
Simulation fast clock cycles (/1): 27649746
Simulation main clock cycles (/2): 13824873

------------------------------
           HART: 0
------------------------------
Cycles: 13824868
Time: 13824868
Retired instructions: 6384852
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: edn
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 6268306
Real instructions: 4026254
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/edn.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/edn.irom8.hex
Simulation fast clock cycles (/1): 12687010
Simulation main clock cycles (/2): 6343505

------------------------------
           HART: 0
------------------------------
Cycles: 6343500
Time: 6343500
Retired instructions: 4073941
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: huffbench
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 5788948
Real instructions: 2598466
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/huffbench.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/huffbench.irom8.hex
Simulation fast clock cycles (/1): 12656030
Simulation main clock cycles (/2): 6328015

------------------------------
           HART: 0
------------------------------
Cycles: 6328010
Time: 6328010
Retired instructions: 2840277
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: matmult-int
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 5781322
Real instructions: 3183123
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/matmult-int.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/matmult-int.irom8.hex
Simulation fast clock cycles (/1): 11898928
Simulation main clock cycles (/2): 5949464

------------------------------
           HART: 0
------------------------------
Cycles: 5949459
Time: 5949459
Retired instructions: 3266799
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: md5sum
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4038742
Real instructions: 2046781
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/md5sum.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/md5sum.irom8.hex
Simulation fast clock cycles (/1): 8247352
Simulation main clock cycles (/2): 4123676

------------------------------
           HART: 0
------------------------------
Cycles: 4123671
Time: 4123671
Retired instructions: 2089515
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: minver
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 12764924
Real instructions: 4964001
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/minver.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/minver.irom8.hex
Simulation fast clock cycles (/1): 25578012
Simulation main clock cycles (/2): 12789006

------------------------------
           HART: 0
------------------------------
Cycles: 12789001
Time: 12789001
Retired instructions: 4973402
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nbody
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 8075299
Real instructions: 3484767
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nbody.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nbody.irom8.hex
Simulation fast clock cycles (/1): 32295328
Simulation main clock cycles (/2): 16147664

------------------------------
           HART: 0
------------------------------
Cycles: 16147659
Time: 16147659
Retired instructions: 6969472
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nettle-aes
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6990066
Real instructions: 4462512
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nettle-aes.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nettle-aes.irom8.hex
Simulation fast clock cycles (/1): 14179358
Simulation main clock cycles (/2): 7089679

------------------------------
           HART: 0
------------------------------
Cycles: 7089674
Time: 7089674
Retired instructions: 4525975
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nettle-sha256
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6320308
Real instructions: 4030435
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nettle-sha256.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nettle-sha256.irom8.hex
Simulation fast clock cycles (/1): 12670254
Simulation main clock cycles (/2): 6335127

------------------------------
           HART: 0
------------------------------
Cycles: 6335122
Time: 6335122
Retired instructions: 4039637
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nsichneu
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 8268709
Real instructions: 2236759
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nsichneu.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nsichneu.irom8.hex
Simulation fast clock cycles (/1): 16552628
Simulation main clock cycles (/2): 8276314

------------------------------
           HART: 0
------------------------------
Cycles: 8276309
Time: 8276309
Retired instructions: 2238947
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: picojpeg
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 7635002
Real instructions: 4192128
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/picojpeg.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/picojpeg.irom8.hex
Simulation fast clock cycles (/1): 17822606
Simulation main clock cycles (/2): 8911303

------------------------------
           HART: 0
------------------------------
Cycles: 8911298
Time: 8911298
Retired instructions: 4892233
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: primecount
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6123503
Real instructions: 2148523
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/primecount.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/primecount.irom8.hex
Simulation fast clock cycles (/1): 24494776
Simulation main clock cycles (/2): 12247388

------------------------------
           HART: 0
------------------------------
Cycles: 12247383
Time: 12247383
Retired instructions: 4297207
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: qrduino
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 5969691
Real instructions: 3173969
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/qrduino.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/qrduino.irom8.hex
Simulation fast clock cycles (/1): 14347380
Simulation main clock cycles (/2): 7173690

------------------------------
           HART: 0
------------------------------
Cycles: 7173685
Time: 7173685
Retired instructions: 3813294
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: sglib-combined
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6648371
Real instructions: 2629387
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/sglib-combined.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/sglib-combined.irom8.hex
Simulation fast clock cycles (/1): 13798822
Simulation main clock cycles (/2): 6899411

------------------------------
           HART: 0
------------------------------
Cycles: 6899406
Time: 6899406
Retired instructions: 2727807
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: slre
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6569232
Real instructions: 2590543
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/slre.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/slre.irom8.hex
Simulation fast clock cycles (/1): 13259268
Simulation main clock cycles (/2): 6629634

------------------------------
           HART: 0
------------------------------
Cycles: 6629629
Time: 6629629
Retired instructions: 2614381
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: st
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 9128440
Real instructions: 3931417
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/st.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/st.irom8.hex
Simulation fast clock cycles (/1): 19667476
Simulation main clock cycles (/2): 9833738

------------------------------
           HART: 0
------------------------------
Cycles: 9833733
Time: 9833733
Retired instructions: 4235169
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: statemate
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 2682894
Real instructions: 1317876
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/statemate.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/statemate.irom8.hex
Simulation fast clock cycles (/1): 5371448
Simulation main clock cycles (/2): 2685724

------------------------------
           HART: 0
------------------------------
Cycles: 2685719
Time: 2685719
Retired instructions: 1319407
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: tarfind
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 2503919
Real instructions: 1037257
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/tarfind.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/tarfind.irom8.hex
Simulation fast clock cycles (/1): 5136890
Simulation main clock cycles (/2): 2568445

------------------------------
           HART: 0
------------------------------
Cycles: 2568440
Time: 2568440
Retired instructions: 1064151
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: ud
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 8686310
Real instructions: 3358071
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/ud.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/ud.irom8.hex
Simulation fast clock cycles (/1): 17389144
Simulation main clock cycles (/2): 8694572

------------------------------
           HART: 0
------------------------------
Cycles: 8694567
Time: 8694567
Retired instructions: 3361307
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: wikisort
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 3078491
Real instructions: 1267935
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/wikisort.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/wikisort.irom8.hex
Simulation fast clock cycles (/1): 12369794
Simulation main clock cycles (/2): 6184897

------------------------------
           HART: 0
------------------------------
Cycles: 6184892
Time: 6184892
Retired instructions: 2539847
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: aha-mont64
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 8684328
Real instructions: 4531262
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/aha-mont64.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/aha-mont64.irom8.hex
Simulation fast clock cycles (/1): 17410928
Simulation main clock cycles (/2): 8705464

------------------------------
           HART: 0
------------------------------
Cycles: 8705459
Time: 8705459
Retired instructions: 4542231
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: crc32
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 6794323
Real instructions: 3831160
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/crc32.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/crc32.irom8.hex
Simulation fast clock cycles (/1): 13669594
Simulation main clock cycles (/2): 6834797

------------------------------
           HART: 0
------------------------------
Cycles: 6834792
Time: 6834792
Retired instructions: 3853897
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: cubic
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 12567004
Real instructions: 5803827
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/cubic.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/cubic.irom8.hex
Simulation fast clock cycles (/1): 27649746
Simulation main clock cycles (/2): 13824873

------------------------------
           HART: 0
------------------------------
Cycles: 13824868
Time: 13824868
Retired instructions: 6384852
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: edn
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 6268306
Real instructions: 4026254
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/edn.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/edn.irom8.hex
Simulation fast clock cycles (/1): 12687010
Simulation main clock cycles (/2): 6343505

------------------------------
           HART: 0
------------------------------
Cycles: 6343500
Time: 6343500
Retired instructions: 4073941
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: huffbench
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 5788948
Real instructions: 2598466
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/huffbench.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/huffbench.irom8.hex
Simulation fast clock cycles (/1): 12656030
Simulation main clock cycles (/2): 6328015

------------------------------
           HART: 0
------------------------------
Cycles: 6328010
Time: 6328010
Retired instructions: 2840277
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: matmult-int
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 5781322
Real instructions: 3183123
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/matmult-int.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/matmult-int.irom8.hex
Simulation fast clock cycles (/1): 11898928
Simulation main clock cycles (/2): 5949464

------------------------------
           HART: 0
------------------------------
Cycles: 5949459
Time: 5949459
Retired instructions: 3266799
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: md5sum
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4038742
Real instructions: 2046781
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/md5sum.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/md5sum.irom8.hex
Simulation fast clock cycles (/1): 8247352
Simulation main clock cycles (/2): 4123676

------------------------------
           HART: 0
------------------------------
Cycles: 4123671
Time: 4123671
Retired instructions: 2089515
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: minver
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 12764924
Real instructions: 4964001
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/minver.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/minver.irom8.hex
Simulation fast clock cycles (/1): 25578012
Simulation main clock cycles (/2): 12789006

------------------------------
           HART: 0
------------------------------
Cycles: 12789001
Time: 12789001
Retired instructions: 4973402
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nbody
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 8075299
Real instructions: 3484767
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nbody.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nbody.irom8.hex
Simulation fast clock cycles (/1): 32295328
Simulation main clock cycles (/2): 16147664

------------------------------
           HART: 0
------------------------------
Cycles: 16147659
Time: 16147659
Retired instructions: 6969472
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nettle-aes
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6990066
Real instructions: 4462512
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nettle-aes.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nettle-aes.irom8.hex
Simulation fast clock cycles (/1): 14179358
Simulation main clock cycles (/2): 7089679

------------------------------
           HART: 0
------------------------------
Cycles: 7089674
Time: 7089674
Retired instructions: 4525975
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nettle-sha256
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6320308
Real instructions: 4030435
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nettle-sha256.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nettle-sha256.irom8.hex
Simulation fast clock cycles (/1): 12670254
Simulation main clock cycles (/2): 6335127

------------------------------
           HART: 0
------------------------------
Cycles: 6335122
Time: 6335122
Retired instructions: 4039637
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nsichneu
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 8268709
Real instructions: 2236759
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nsichneu.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/nsichneu.irom8.hex
Simulation fast clock cycles (/1): 16552628
Simulation main clock cycles (/2): 8276314

------------------------------
           HART: 0
------------------------------
Cycles: 8276309
Time: 8276309
Retired instructions: 2238947
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: picojpeg
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 7635002
Real instructions: 4192128
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/picojpeg.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/picojpeg.irom8.hex
Simulation fast clock cycles (/1): 17822606
Simulation main clock cycles (/2): 8911303

------------------------------
           HART: 0
------------------------------
Cycles: 8911298
Time: 8911298
Retired instructions: 4892233
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: primecount
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6123503
Real instructions: 2148523
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/primecount.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/primecount.irom8.hex
Simulation fast clock cycles (/1): 24494776
Simulation main clock cycles (/2): 12247388

------------------------------
           HART: 0
------------------------------
Cycles: 12247383
Time: 12247383
Retired instructions: 4297207
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: qrduino
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 5969691
Real instructions: 3173969
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/qrduino.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/qrduino.irom8.hex
Simulation fast clock cycles (/1): 14347380
Simulation main clock cycles (/2): 7173690

------------------------------
           HART: 0
------------------------------
Cycles: 7173685
Time: 7173685
Retired instructions: 3813294
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: sglib-combined
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6648371
Real instructions: 2629387
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/sglib-combined.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/sglib-combined.irom8.hex
Simulation fast clock cycles (/1): 13798822
Simulation main clock cycles (/2): 6899411

------------------------------
           HART: 0
------------------------------
Cycles: 6899406
Time: 6899406
Retired instructions: 2727807
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: slre
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6569232
Real instructions: 2590543
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/slre.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/slre.irom8.hex
Simulation fast clock cycles (/1): 13259268
Simulation main clock cycles (/2): 6629634

------------------------------
           HART: 0
------------------------------
Cycles: 6629629
Time: 6629629
Retired instructions: 2614381
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: st
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 9128440
Real instructions: 3931417
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/st.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/st.irom8.hex
Simulation fast clock cycles (/1): 19667476
Simulation main clock cycles (/2): 9833738

------------------------------
           HART: 0
------------------------------
Cycles: 9833733
Time: 9833733
Retired instructions: 4235169
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: statemate
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 2682894
Real instructions: 1317876
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/statemate.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/statemate.irom8.hex
Simulation fast clock cycles (/1): 5371448
Simulation main clock cycles (/2): 2685724

------------------------------
           HART: 0
------------------------------
Cycles: 2685719
Time: 2685719
Retired instructions: 1319407
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: tarfind
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 2503919
Real instructions: 1037257
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/tarfind.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/tarfind.irom8.hex
Simulation fast clock cycles (/1): 5136890
Simulation main clock cycles (/2): 2568445

------------------------------
           HART: 0
------------------------------
Cycles: 2568440
Time: 2568440
Retired instructions: 1064151
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: ud
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 8686310
Real instructions: 3358071
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/ud.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/ud.irom8.hex
Simulation fast clock cycles (/1): 17389144
Simulation main clock cycles (/2): 8694572

------------------------------
           HART: 0
------------------------------
Cycles: 8694567
Time: 8694567
Retired instructions: 3361307
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: wikisort
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 3078491
Real instructions: 1267935
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/wikisort.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb8IFReg/wikisort.irom8.hex
Simulation fast clock cycles (/1): 12369794
Simulation main clock cycles (/2): 6184897

------------------------------
           HART: 0
------------------------------
Cycles: 6184892
Time: 6184892
Retired instructions: 2539847
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------



"""

extract_cpi(report_data)
