
"""Prepares all the files according to the other four scripts
for seq, json, inp and slurm file preparation"""

# Prepares sequences for SR
exec(open("create_sr_seq.py").read())

# Prepares JSON config files
exec(open("create_sr_jsons.py").read())

# Prepares configuration input files
exec(open("create_sr_input-configs.py").read())

# Prepares SLURM batch jobs
exec(open("create_sr_slurms.py").read())

# Prepares the simulation folders
exec(open("create_sr_folders.py").read())
