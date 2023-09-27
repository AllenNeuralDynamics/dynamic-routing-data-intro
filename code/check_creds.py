#!/usr/bin/env python3
import npc_lims

print('checking Codeocean API credentials...', end='\t', flush=True)
try:
    assert len(npc_lims.get_subject_data_assets(668759)) > 0
except:
    print('failed!')
else:
    print('success!')

print('checking AWS credentials...', end='\t\t', flush=True)
try:
    assert len(tuple(npc_lims.DR_DATA_REPO.iterdir())) > 0
except:
    print('failed!')
else:
    print('success!')
