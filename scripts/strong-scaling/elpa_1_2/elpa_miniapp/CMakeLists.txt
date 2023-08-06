cmake_minimum_required(VERSION 3.18)

project(elpa-miniapp LANGUAGES C)

find_package(MPI REQUIRED)

#set(EBROOTELPA "/p/project/cslai/wu/install/mathlib/juwelsbooster/elpa-new_release_2022.11.001.rc1/install")
#set(ELPA_INCLUDE "/p/project/cslai/wu/install/mathlib/juwelsbooster/elpa-new_release_2022.11.001.rc1/install/include/elpa_openmp-2022.11.001.rc1/")
#set(ELPA_MODULES "/p/project/cslai/wu/install/mathlib/juwelsbooster/elpa-new_release_2022.11.001.rc1/install/include/elpa_openmp-2022.11.001.rc1/modules")

set(EBROOTELPA "${CMAKE_SOURCE_DIR}/../elpa/install")
set(ELPA_INCLUDE "${EBROOTELPA}/include/elpa_openmp-2022.11.001.rc1/")
set(ELPA_MODULES "${EBROOTELPA}/include/elpa_openmp-2022.11.001.rc1/modules")

message(STATUS "EBROOTELPA: " ${EBROOTELPA})
message(STATUS "ELPA_INCLUDE: " ${ELPA_INCLUDE})
message(STATUS "ELPA_MODULES: " ${ELPA_MODULES})


add_executable( "elpa.exe" elpa-miniapp.c )
target_link_libraries("elpa.exe" 
	PUBLIC 
		${EBROOTELPA}/lib/libelpa_openmp.so
		MPI::MPI_C
		m
		)

target_include_directories("elpa.exe" 
	PUBLIC
		${ELPA_INCLUDE}
		${ELPA_INCLUDE}elpa
		${ELPA_MODULES}
		)

