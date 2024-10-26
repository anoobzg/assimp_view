message(STATUS "The CMake version used is ${CMAKE_VERSION}")
cmake_minimum_required(VERSION 3.15...${CMAKE_VERSION})

project(assimp_view)

include(cmake/entry/desktop-cpp.cmake)
__install_conan_requirements(MSVC_RUNTIME "static")

find_package(SDL2 CONFIG REQUIRED)
find_package(assimp CONFIG REQUIRED)

SET(OSRE_BUILD_ED OFF CACHE BOOL "no osre ed" )

add_subdirectory(osre)

INCLUDE_DIRECTORIES( BEFORE
    ./
    src
	osre/src/Engine
    osre/contrib/cppcore/include
	${SDL2_INCLUDE_DIRS}
    ${PROJECT_SOURCE_DIR}
)

link_directories(
    ${SDL2_LIBRARIES}
)

set(assimpview_main_src
    src/main.cpp
    src/ModelLoadingApp.h
    src/ModelLoading.cpp
    src/SceneData.h
)

SOURCE_GROUP(Main\\    FILES ${assimpview_main_src})

ADD_EXECUTABLE( assimp_view
    ${assimpview_main_src}
)

target_link_libraries(assimp_view
	PRIVATE SDL2::SDL2 assimp::assimp osre
)

__modify_target(assimp_view)
__modify_target(Unzip)
__modify_target(cppcore)
__modify_target(cppcore_unittest)
__modify_target(gmock)
__modify_target(gmock_main)
__modify_target(gtest)
__modify_target(gtest_main)
__modify_target(osre)