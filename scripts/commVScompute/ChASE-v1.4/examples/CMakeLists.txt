set(subdirs
	  0_hello_world
    1_sequence_eigenproblems
    2_input_output
    4_interface
)

foreach(subdir ${subdirs})
  add_subdirectory(${subdir})
endforeach()

