#!/usr/bin/env bash

USER=rinzler
GRID_HOME_DIR=/home/${USER}/GridShowBox


#Check if FS exists at user home and if not, create it
mainFSCheck(){
    echo "The Grid Show Box dir Check"
[[ ! -d $GRID_HOME_DIR ]] && mkdir $GRID_HOME_DIR 
}

mainFSCheck

#check if TheGrid directory exists within GridShowBox
theGridDirCheck(){
    echo "The Grid Dir Check"
    [[ ! -d ${GRID_HOME_DIR}/TheGrid]] && mkdir ${GRID_HOME_DIR}/TheGrid
}

theGridDirCheck

#check if TheGrid category directories exist
theGridCatCheck(){
    echo 'The Grid Cats Check'
    [[ ! -d ${GRID_HOME_DIR}/TheGrid/TV]] && mkdir ${GRID_HOME_DIR}/TheGrid/TV ${GRID_HOME_DIR}/TheGrid/TV/Genre ${GRID_HOME_DIR}/TheGrid/TV/Genre/Action ${GRID_HOME_DIR}/TheGrid/TV/Genre/Comedy ${GRID_HOME_DIR}/TheGrid/TV/Genre/Drama ${GRID_HOME_DIR}/TheGrid/TV/Genre/Fantasy ${GRID_HOME_DIR}/TheGrid/TV/Genre/Horror ${GRID_HOME_DIR}/TheGrid/TV/Genre/Romance
#    [[ ! -d ${GRID_HOME_DIR}/TheGrid/Movies]] && mkdir ${GRID_HOME_DIR}/TheGrid/Movies ${GRID_HOME_DIR}/TheGrid/Movies/Genre ${GRID_HOME_DIR}/TheGrid/Movies/Genre/Action ${GRID_HOME_DIR}/TheGrid/Movies/Genre/Comedy ${GRID_HOME_DIR}/TheGrid/Movies/Genre/Drama ${GRID_HOME_DIR}/TheGrid/Movies/Genre/Fantasy ${GRID_HOME_DIR}/TheGrid/Movies/Genre/Horror ${GRID_HOME_DIR}/TheGrid/Movies/Genre/Romance
#    [[ ! -d ${GRID_HOME_DIR}/TheGrid/Commercials]] && mkdir ${GRID_HOME_DIR}/TheGrid/Commercials ${GRID_HOME_DIR}/TheGrid/Commercials/Genre ${GRID_HOME_DIR}/TheGrid/Commercials/Genre/Action ${GRID_HOME_DIR}/TheGrid/Commercials/Genre/Comedy ${GRID_HOME_DIR}/TheGrid/Commercials/Genre/Drama ${GRID_HOME_DIR}/TheGrid/Commercials/Genre/Fantasy ${GRID_HOME_DIR}/TheGrid/Commercials/Genre/Horror ${GRID_HOME_DIR}/TheGrid/Commercials/Genre/Romance
}

theGridCatCheck


workspaceCheck(){
    [[ ! -d ${GRID_HOME_DIR}/workspace ]] && mkdir ${GRID_HOME_DIR}/workspace
}

