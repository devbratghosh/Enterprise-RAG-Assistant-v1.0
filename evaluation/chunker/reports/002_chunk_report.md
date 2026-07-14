# Chunking Experiment Report

## Execution

| Property | Value |
|---|---|
| Run | 2 |
| Date | 13-Jul-2026 |
| Time | 12:26:09 PM |
| Duration (sec) | 2.042 |

---

## Configuration

| Setting | Value |
|---|---|
| Version | 1.0.0 |
| Strategy | Recursive |
| Chunk Size | 500 |
| Overlap Strategy | Section Boundary |
| Overlap Size | 50 |
| Embedding Model | all-MiniLM-L6-v2 |
| Collection | enterprise_policies |
| Top K | 3 |

## Document Statistics

| Metric | Value |
|---|---|
| Document | policy.pdf |
| Characters | 67031 |
| Words | 9266 |
| Lines | 1149 |
| Paragraphs | 98 |
| Chapters | 47 |
| Sections | 98 |

## Chunk Statistics

| Metric | Value |
|---|---|
| Chunks | 121 |
| Average Size | 649.09 |
| Median Size | 741 |
| Largest | 800 |
| Smallest | 186 |
| Invalid | 0 |
| Duplicate | 0 |
| Empty | 0 |

## Validation

Overall Status: **FAILED**

- 51 chunk(s) end mid-sentence.

## Execution Timeline

| Timestamp | Event | Description |
|---|---|---|
| 13-Jul-2026 12:26:09 PM | Chunking Started | Chunk generation started. |
| 13-Jul-2026 12:26:11 PM | Chunking Completed | Chunk generation completed. |
| 13-Jul-2026 12:26:11 PM | Validation Completed | Chunk validation completed. |
| 13-Jul-2026 12:26:11 PM | History Updated | Experiment history updated. |
| 13-Jul-2026 12:26:11 PM | Report Generated | Markdown report generated. |

## Engineering Notes



## Future Recommendation



## Engineering Decision

**Needs Investigation**

