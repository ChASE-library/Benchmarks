set(subdirs
    2_input_output
)

foreach(subdir ${subdirs})
  add_subdirectory(${subdir})
endforeach()

