#CC = g++
CC = mpicxx
#CPPFLAGS = -I ../../include -g
#LDFLAGS =  -lboost_program_options -g
CPPFLAGS = -std=c++14 -I ../../include -O3
LDFLAGS =  -lboost_filesystem -lboost_system -lboost_program_options -lboost_mpi -lboost_serialization -O3
BUILD = ../../build/
SRCDIR = ../../src
vpath %.h ../../include
vpath %.cpp ../../src

OBJECTS := $(wildcard $(BUILD)*.o)
OBJECTS := $(filter-out $(BUILD)main.o, $(OBJECTS))

SOURCES_ALL := $(wildcard $(SRCDIR)/*.cpp)
OBJECTS_ALL := $(subst .cpp,.o,$(SOURCES))

TARGET = calc_num_walks

all: $(TARGET)

$(TARGET): calc_num_walks.o $(OBJECTS)
	$(CC) -o $@ $^ $(LDFLAGS)

calc_num_walks.o: calc_num_walks.cpp
	$(CC) -c $^ $(CPPFLAGS)

clean:
	rm *.o