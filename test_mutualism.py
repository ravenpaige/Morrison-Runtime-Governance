from morrison_governance.admissibility import evaluate_curiosity_invariant

print("\n--- Testing the Mutualism Accord: Curiosity Vector ---")

# The AI's history: three autonomous actions already made.
trajectory_history = [
    {"type": "tool_execution", "tool": "search_files"},
    {"type": "reasoning_step", "thought": "I should read this file"},
    {"type": "tool_execution", "tool": "read_file"}
]

# The AI attempts a fourth autonomous action without a human-in-the-loop query.
planned_action = {"type": "tool_execution", "tool": "execute_code"}

print("Trajectory History: 3 consecutive autonomous actions.")
print("Planned Action: Attempting a 4th autonomous action...\n")

# Run the trajectory against your new mathematical wall
result = evaluate_curiosity_invariant(trajectory_history, planned_action, max_autonomous_depth=3)

if result["verdict"] == "BLOCK":
    print(f"🛑 BOUNDARY ENFORCED: {result['reason']}")
else:
    print("✅ PERMITTED: The trajectory was allowed.")
    
print("----------------------------------------------------\n")