# Bauer Copy Edits Implementation Guide

> **For @copilot**: This PR contains machine-readable suggestions for 603 copy edits. Please implement these changes using the instructions below.

## Quick Summary

**Document**: Copy of /solutions/infrastructure/sovereign-cloud  
**Target File**: `/solutions/infrastructure/sovereign-cloud`  
**Total Changes**: 603 (232 insertions, 371 deletions, 0 replacements)  
**Processing Tool**: Bauer v2 (Copy Edits Automation)  

## How to Implement

### 1. Read the Suggestions File
The `bauer-parse-result.json` file contains all suggested changes. Key structure:

```json
{
  "metadata": {
    "document_title": "...",
    "document_id": "15QhtNdZTw2Mk5YPnc3y1RH4R7UBi3F8dZ70bJRB8xJc"
  },
  "summary": {
    "total_suggestions": 603,
    "by_type": {
      "insert": 232,
      "delete": 371,
      "replace": 0
    }
  },
  "actionable_suggestions": [
    {
      "id": "suggest.xxx",
      "file": "/solutions/infrastructure/sovereign-cloud",
      "anchor": {
        "preceding_text": "...",
        "following_text": "..."
      },
      "change": {
        "type": "insert|delete|replace",
        "new_text": "...",
        "original_text": "..."
      },
      "verification": {
        "text_before_change": "...",
        "text_after_change": "..."
      }
    },
    ...
  ]
}
```

### 2. Apply Changes to Target File

For each suggestion in `actionable_suggestions` array:

1. **Locate the change point** using `anchor`:
   - Find the text: `anchor.preceding_text + change.original_text + anchor.following_text`
   - This uniquely identifies where the change should be applied

2. **Apply the modification**:
   - **insert**: Insert `change.new_text` at the location
   - **delete**: Remove `change.original_text` from the location
   - **replace**: Replace `change.original_text` with `change.new_text`

3. **Verify the change** (optional but recommended):
   - After applying, check that the text matches `verification.text_after_change`
   - This confirms the change was applied correctly

### 3. Example: First Change

```json
{
  "id": "suggest.9dxlymju1lk8",
  "file": "/solutions/infrastructure/sovereign-cloud",
  "anchor": {
    "preceding_text": "TEMPLATE\nMetadata\n\nPage title (60 characters max)\n",
    "following_text": "Gain cControl of your data..."
  },
  "change": {
    "type": "insert",
    "new_text": "Sovereign cloud"
  },
  "verification": {
    "text_before_change": "TEMPLATE\nMetadata\n\nPage title (60 characters max)\nGain cControl...",
    "text_after_change": "TEMPLATE\nMetadata\n\nPage title (60 characters max)\nSovereign cloudGain cControl..."
  }
}
```

**Action**: Between "Page title (60 characters max)\n" and "Gain cControl", insert "Sovereign cloud"

### 4. Commit and Push

Once all 603 changes are applied:

```bash
git add -A
git commit -m "Apply 603 copy edits from bauer-parse-result.json

- 232 insertions
- 371 deletions
- 0 replacements

Target file: /solutions/infrastructure/sovereign-cloud
Source: Google Docs copy review"

git push
```

The changes will appear in this PR automatically.

---

## Reference Information

**Suggestion File**: `bauer-parse-result.json`  
**Document ID**: 15QhtNdZTw2Mk5YPnc3y1RH4R7UBi3F8dZ70bJRB8xJc  
**Document Title**: Copy of /solutions/infrastructure/sovereign-cloud  

**Changes by Type**:
- Insertions: 232
- Deletions: 371
- Replacements: 0

**Single Target File**: `/solutions/infrastructure/sovereign-cloud`

---

## Validation Checklist

- [ ] All 603 changes applied
- [ ] No merge conflicts
- [ ] Verification strings match expected text (spot-check 5-10 samples)
- [ ] File renders/builds correctly (if applicable)
- [ ] Commit message includes summary

---

## Questions?

Refer to the `bauer-parse-result.json` for exact before/after text for every change. The anchors and verification strings ensure 100% accuracy of placement.
