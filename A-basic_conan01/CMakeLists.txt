cmake_minimum_required (VERSION 3.5)

project(subprojects)

# Add sub directories
if(SUBLIBRARY1_RUN) 
    add_subdirectory(sublibrary1)
endif()
if(SUBLIBRARY2_RUN) 
    add_subdirectory(sublibrary2)
endif()
if(SUBBINARY_RUN) 
    add_subdirectory(subbinary)
endif()
