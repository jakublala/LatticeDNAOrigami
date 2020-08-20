#CC = g++
CC = mpicxx
#CPPFLAGS = -I ../../include -g
#LDFLAGS =  -lboost_program_options -g
CPPFLAGS = -std=c++14 -I ../../include -O3
LDFLAGS =  -lboost_filesystem -lboost_system -lboost_program_options -lboost_mpi -lboost_serialization -O3
BUILD = ../../build/
vpath %.h ../../include
vpath %.cpp ../../src
#OBJECTS := $(wildcard $(BUILD)*.o)
#OBJECTS := $(filter-out $(BUILD)main.o, $(OBJECTS)))

TARGET = calc_num_walks

all: $(TARGET)

$(TARGET): calc_num_walks.o $(BUILD)origami_system.o $(BUILD)utility.o $(BUILD)nearest_neighbour.o $(BUILD)files.o $(BUILD)jsoncpp.o $(BUILD)origami_potential.o $(BUILD)order_params.o $(BUILD)bias_functions.o $(BUILD)top_constraints_points.o $(BUILD)domain.o $(BUILD)simulation.o $(BUILD)parser.o $(BUILD)random_gens.o $(BUILD)movetypes.o $(BUILD)ideal_random_walk.o
	$(CC) -o $@ $^ $(LDFLAGS)

calc_num_walks.o: calc_num_walks.cpp
	$(CC) -c $^ $(CPPFLAGS)

clean:
	rm *.o