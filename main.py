from typing import List
import functions_framework

@functions_framework.http
def generate_random_sequence(request):
    # extract the input parameters from the request
    request_json = request.get_json()
    m = request_json['m']
    n = request_json['n']
    
    # generate the random sequence
    import random
    sequence = [random.randint(1, n) for _ in range(m)]
    
    # return the generated sequence
    return sequence


"""
We shall turn this script into a library of `functions_framework` related code units that will run in parallel (new processes are simply join already parallel units)

    For example, I was forgetting that `reversibile-computation` unit and I would like someone to reach me with the information.
    For example, here is the complete (almost) description for a starting code in modeling dynamical processes; nonetheless this was
    a miracle that I was able to collect togehter the bits of thoughts that have been popping in/out since yesterday.
        ```python
        import torch
        
        # model types are continuous, descrete, others
        # the continuous models are for the purpose of managing `extreme-supervision` tasks.

        #1# supervision: this is a process that is carried out by an assigned `operator` that has a criterion which must be activated in order to evaluate runtime of such script.,
        # [note] the above scripts are only runtime and staying active during a specified runtime allocation certain energy minimum must be maintained other wise terminated forefully.
        #2# extreme-supervision: these tasks may be composed of multiple generic supervision events, perhaps a network which controls from a hyperspace.

        ## up to this point what got covered:
        ### [the possibility of different signal handling/processing/managing events]
        ### [a primary constraint system that the minimum kernel for all systems under `Luminol` (which is our main organization]
        ### [possible demands on the evolution of such processes.-0]
"""

## for every signal stream
## find all the identities
## hence information is all of (every stream, identities), (every stream / identities)
"""
def main():
    # load state for 2-port (left-node)
    left_node = load_state_state("/")
    right_node = left_node.build_code()
    main_circuit = restore_statespace(execute(source=right_node, environment=left_node))
    memory, processor, operators = main_circuit.get_objects()
    controllers = operators.get_objects()
    stereo_waveform = processor.compile()

    for pointer in controllers:
        pan, gain, seperation, connection_matrix = memory[pointer]
        stereo_waveform[connection_matrix] += update_signal(pan, gain, seperation)

"""