# Pilot review

Both responses are preserved. Both contain ten judgments and pass the structural validator. The documents pilot used 8,394 input and 1,626 output tokens; the repository pilot used 38,170 input and 1,641 output tokens, including repeated context. Usage figures are from completion events and include 817 reasoning output tokens across the two sessions.

The repository pilot called list_files once; the call failed because approval was required while the policy was never. It completed from supplied documents. It is a delivery failure, not a successful repository pilot. No replacement was generated. The first main repository session must be checked for successful source calls.

The documents response gave A4 a partial rating and said no Python version constraint was given while quoting “Python 3.” This is an assistant identified tension, not a validated error count. B2 gave a full rating while noting that the procedure was only described as two checks. These examples show that structural validity is not sufficient. Pilot findings did not change rubric anchors or establish benchmark reference ratings.

Harness changes before main freeze: replace ignored tools.view_image setting with features.view_image; mark file tools read only; set automatic approval only for the two confined file tools. Pilot source files and outputs are unchanged. Offline tests verify valid reads and rejection of traversal and symlink escapes. Human review: none.
