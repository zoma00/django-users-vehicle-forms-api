vehicle_data=$(curl http://127.0.0.1:8000/api/vehicle/ | sed '/^$/d')  # Remove empty lines (optional)
vehicle_info=$(echo "${vehicle_data}" | jq -r '.[].id, .[].type_name')

# Split the combined output into separate variables for clarity
IFS=',' read -ra vehicle_details <<< "${vehicle_info}"

for i in "${!vehicle_details[@]}"; do
  if [[ $((i % 2)) -eq 0 ]]; then
    vehicle_id="${vehicle_details[$i]}"
  else
    type_name="${vehicle_details[$i]}"
    echo "Vehicle ID: ${vehicle_id}"
    echo "Related Vehicle Type: ${type_name}"
    echo ""  # Add an empty line for readability
  fi
done
