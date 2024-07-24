import re

def extract_cpi(report):

    exec_blocks = re.findall(r"EXEC NAME: (.+?)\n.*?Real cycles: (\d+).*?Real instructions: (\d+)", report, re.DOTALL)

    for exec_name, cycles, instructions in exec_blocks:

        cycles = int(cycles)
        instructions = int(instructions)


        cpi = cycles / instructions if instructions != 0 else float('inf')


        print(f"{exec_name}: CPI = {cpi:.3f}")


report_data = """


"""

extract_cpi(report_data)
