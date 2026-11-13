---
title: MBON-α1（α1 輸出神經元）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# MBON-α1（α1 輸出神經元）


**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蕈狀體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」（α、α′、β、β′、γ），每條葉沿長度切成一格一格的「區室」；α1 是 α 葉最靠近根部的一格。細胞以所在區室命名。見 [[e-mushroom-body]]、[[c-mb-compartment]]。
- **MBON**：蕈狀體輸出神經元，接收 KC 的訊號、把結果送出蕈狀體；學習改變的是 KC→MBON 突觸的強弱（見 [[e-mbon]]）。
- **DAN、PAM**：多巴胺神經元（dopaminergic neuron）送出代表獎賞或懲罰的多巴胺；PAM 群多傳遞獎賞。PAM-α1 是送多巴胺進 α1 的那一型（[[e-pam-alpha1]]）。
- **CS+／CS−**：訓練時配了糖或 DAN 活化的氣味（CS+），與沒配的對照氣味（CS−）。
- **STM、LTM**：短期記憶（Ichinose 2015 指訓練後 5 分鐘測得）與長期記憶（指 24 小時後測得）。
- **LI、PI**：行為分數，一群果蠅在兩種氣味間選擇換算成的一個數，0＝沒有偏好（見 [[c-performance-index]]）。
- **驅動品系**：讓外加基因只在選定神經元表現的果蠅品系；split-GAL4 把 GAL4 拆成兩半，兩半都在的細胞才有作用（[[e-split-gal4]]）。基因型「X/+」是只帶一個品系的對照組。
- **工具**：CsChrimson 照紅光讓神經元放電（[[e-cschrimson]]）；dTrpA1 遇熱讓神經元放電（`e-dtrpa1`）；shibire^ts1（shi）升溫時暫時關掉神經元的輸出（[[e-shibire-ts]]）；GRASP 檢驗兩顆細胞的膜是否緊貼（[[e-grasp]]）；全細胞記錄＝把玻璃電極接上細胞、直接量電位（[[c-whole-cell-patch-clamp]]）。
- **連結體、hemibrain**：用電子顯微鏡重建的全腦接線圖；hemibrain 是其中一份（[[e-hemibrain]]）。「兩跳」＝中間隔兩個神經元的路徑。
- **UpWiN**：Aso 2023 命名的一群「迎風神經元」，活化時果蠅轉向上風。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值；「該頁」指表格同一列的來源頁。

## 是什麼

**MBON-α1 是樹突在蕈狀體 α1 區室的輸出神經元，用麩胺酸（glutamate）傳訊，每側腦 2 顆。** 短名 MBON-07（Aso 2014b 表 1；hemibrain 寫 MBON07），與 MBON-γ4>γ1γ2、MBON-β1>α 同屬細胞體聚在一起的 MV2 群（Aso 2014b）。同一格的 DAN 是 [[e-pam-alpha1]]。在本庫它以兩件事出名：Ichinose 2015 的「PAM-α1 → KC → MBON-α1 → PAM-α1」迴圈，被認為是獎賞長期記憶形成所需；Yamada 2023 與 Aso 2023 則把它接到別格的 DAN 與迎風行為。依 Yamada 2023（引 Li 2020），它是唯一一型不直接接到其他區室 DAN 的 MBON，只接回同格的 PAM-α1。

## 版本與規模（標記它的品系）

| 品系 | 來源 | 說明 |
|---|---|---|
| **MB310C**（split-GAL4） | Aso 2014b 圖 2C、7；Ichinose 2015 全篇；Aso 2023 圖 2A、4B | 只標這一型；Aso 2014b 唯一一條 α1 品系 |
| MB323B（split-GAL4） | Ichinose 2015 圖 3、8、9 | 第二條品系，由 Ichinose 2015 補上（品系來源 Aso 2014a） |

細胞數：Aso 2014b 表 1 為 2 顆；Ichinose 2015 以 MCFO 多色標記也看到 2 顆、「形態非常相似」；Aso 2023 在 hemibrain 右腦數到 2 顆。數值見 [[numbers]]。

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-aso-2014-mb-architecture]] | 以 split-GAL4 與免疫染色做解剖分類（圖 14、20） | 歸為麩胺酸性，但 dVGluT 染色「遠弱於」其他麩胺酸性 MBON（圖 14N）；PAM-α1 的末梢略微超出它的樹突範圍（14O）；它的末梢與膽鹼性 MBON-α3 的末梢在次微米距離內重疊（圖 20） |
| [[s-aso-2014-mbon-valence]] | MB310C 驅動 CsChrimson 活化未受訓練的果蠅（圖 2C）；MB310C 驅動 shi 阻斷，量 2 小時氣味—糖記憶（圖 7） | 活化：沒有偏好，中位數約 0。阻斷：2 小時獎賞記憶顯著受損（\*\*）。只有一條品系，依該篇方法只算「提示性」，圖 13 卻以實心標示 |
| [[s-ichinose-2015-reward-recurrent-circuit]] | MB310C、MB323B；光學顯微解剖與 GRASP；shi 在訓練時、訓練後、測試時阻斷；dTrpA1 活化；在它身上降低 DopR1 | 末梢貼在 PAM-α1 的樹突旁（SIP、SLP），GRASP 有訊號。訓練時阻斷：5 分鐘記憶不顯著，24 小時記憶剩對照的約 34%（MB310C）、44%（MB323B）；訓練後 0–1 小時阻斷剩約 24%，22 小時後阻斷無效；測試時阻斷 LI 約 0.09、0.12，對照約 0.28–0.29；不給糖、活化它 1 分鐘配氣味，24 小時 LI 約 0.15，對照約 −0.05 與 0.00；降低它的 DopR1 不影響（皆 ※ 從圖判讀） |
| [[s-yamada-2023-second-order-conditioning]] | hemibrain 找它到 DAN 的兩跳路徑；活體全細胞記錄 | 主路是 MBON-α1 →（SMP353／SMP354）→ SMP108 → 多型獎賞 DAN。正文報告光活化 PAM-α1 配氣味後，它對該氣味的反應被壓低（資料在未取得的補充圖 3-2）；機制假設它的麩胺酸對下游是抑制，未直接測 |
| [[s-aso-2023-upwind-neurons]] | hemibrain 連結數；MB310C 驅動 Chrimson88 光活化，全細胞記錄 UpWiN；離體鈣成像；單獨活化看迎風 | 2 顆 → SMP354 共 268 個突觸、→ SMP353 共 67 個；活化它讓 17 顆 UpWiN 中 4 顆（12 隻）被抑制；鈣成像看不到下降；單獨活化不引起迎風 |

Aso 2016 與 Kaldun 2025 只在討論或引言引用 Ichinose 2015 的迴圈，沒有操作它，不列入表。

## 已知的問題

- **它推動靠近還是走開，各頁讀法不同。** Aso 2014b 活化 MB310C 沒有偏好，卻是獎賞記憶所需；該來源頁說它的角色是「價值」還是「回饋給 DAN」仍待直接檢驗。Ichinose 2015 的作者模型（圖 11）是：提取時它經 PAM-α1 以外的下游推動「趨近」。Ichinose 來源頁 3.8 另提一種讀法（它推動走開、學習壓低它對 CS+ 的反應），並註明 Aso 2014b 的活化結果不直接支持這個讀法、但一條品系的陰性結果也不能排除。Aso 2023 則說單獨活化無效與「它抑制 UpWiN」不矛盾。本頁不裁決（見 [[syn-contradictions]] 3.6）。
- **麩胺酸的正負號沒有人在同一個下游量過。** Ichinose 2015 主張它經 PAM-α1 的 NMDA 受體提供**興奮性**回饋；Yamada 2023 的機制需要它對 SMP353/354 是**抑制**；Aso 2023 量到它抑制 UpWiN（SMP353/354 屬於 UpWiN）。下游不同，Yamada 來源頁不列為跨篇矛盾。另外 Aso 2014a 自己對它是麩胺酸性的把握較低（dVGluT 弱）。
- **學習後它對 CS+ 的反應往哪變。** Ichinose 的迴圈需要它在訓練後還能驅動 PAM-α1；Yamada 2023 報告配對後反應下降，但資料在未取得的補充圖、用的是光活化而非真糖（[[syn-contradictions]] 3.6 只填上一半）。Aso 2023 摘要把這一步寫得像自己的觀察，其實是引 Yamada 2023（該頁第五節第 2 條）。
- **阻斷它 ≠ 阻斷回饋。** shi 擋住它送往所有目標的輸出；Ichinose 自己的圖 8 說它另有負責提取的下游。迴圈的突觸連結只有光學相鄰與 GRASP，作者自承「仍待生理學證明」。
- **品系少。** 行為的 dTrpA1 活化、Aso 2014b 的阻斷與活化都只用 MB310C；兩條品系在 Ichinose 的損害程度也不同（34% 對 44%）。

## 相關

- 同格 DAN：[[e-pam-alpha1]]；末梢交會的另一型：[[e-mbon-alpha3]]；細胞：[[e-mbon]]、[[e-dopaminergic-neuron]]
- 品系與工具：[[e-split-gal4]]、[[e-shibire-ts]]、`e-dtrpa1`、[[e-cschrimson]]、[[e-grasp]]、[[e-hemibrain]]
- 概念：[[c-appetitive-memory]]、[[c-memory-consolidation]]、[[c-us-substitution]]、[[c-second-order-conditioning]]、[[c-valence-coding]]、[[c-kc-mbon-plasticity]]
- 主題：[[t-mbon-dan-feedback]]、[[t-mbon-to-action]]；矛盾與未解：[[syn-contradictions]]
- 來源：[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-yamada-2023-second-order-conditioning]]、[[s-aso-2023-upwind-neurons]]
- 待開頁面：`e-mb310c`、`e-upwin`
