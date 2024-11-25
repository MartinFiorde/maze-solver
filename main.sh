#!/bin/bash

# Solicita al usuario las semillas opcionales
read -p "Enter seed1 (or press Enter to use default): " seed1
read -p "Enter seed2 (or press Enter to use default): " seed2

# Construye el comando con los valores proporcionados
command="python3 -m src.main"

# Agrega las semillas solo si se ingresaron valores
if [ -n "$seed1" ]; then
    command+=" $seed1"
fi

if [ -n "$seed2" ]; then
    command+=" $seed2"
fi

# Ejecuta el comando
echo "Executing: $command"
eval $command

echo "Script done. Press Enter to close..."
read