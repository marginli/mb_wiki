---
title: MBON-α2sc（α2sc 輸出神經元）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# MBON-α2sc（α2sc 輸出神經元）


**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蕈狀體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」（α、α′、β、β′、γ），每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、α2、α3）；細胞以所在區室命名。見 [[e-mushroom-body]]、[[c-mb-compartment]]。
- **DAN、PPL1**：多巴胺神經元（dopaminergic neuron）送出代表懲罰或獎賞的多巴胺；PPL1 群多傳遞懲罰（見 [[e-dopaminergic-neuron]]）。
- **MBON**：蕈狀體輸出神經元，接收 KC 的訊號、推動果蠅靠近或走開；學習改變的是 KC→MBON 突觸的強弱（見 [[e-mbon]]）。
- **CS+／CS−**：訓練時配了電擊或 DAN 活化的氣味（CS+），與沒配的對照氣味（CS−）。
- **驅動品系**：讓外加基因只在選定神經元表現的果蠅品系；split-GAL4 把 GAL4 拆成兩半，兩半都在的細胞才有作用（[[e-split-gal4]]）。GAL4 與 LexA 是兩套互不干擾的開關。
- **工具與量法**：CsChrimson 照紅光讓神經元放電（[[e-cschrimson]]）；shibire^ts1 升溫時暫時關掉神經元的輸出（[[e-shibire-ts]]）；全細胞膜片鉗＝把玻璃電極接上細胞、直接量放電（[[c-whole-cell-patch-clamp]]）；電壓成像＝用會隨膜電壓變亮的螢光蛋白（Huang 2024 用 pAce）、每秒拍 1,000 張，看每一次放電。
- **V2 群**：Felsenberg 2017 對 α、α′ 葉上五型 MBON 的合稱（MBON-α2sc、α′1、α2p3p、α′3ap、α′3m）。
- **舊名與新名**：Aso 2014a（[[s-aso-2014-mb-architecture]]）以前，蕈狀體的細胞型多用 Tanaka 2008 的舊名（MB-MP1、MB-V2α 等），同一顆細胞在不同論文裡名字不同；Aso 2014a 改以所在區室命名，並在表 1 給出新舊名對照。
- **光遺傳篩檢（Aso 2014b）**：在沒有訓練、沒有氣味時用紅光活化某型 MBON，看果蠅往照光區靠近還是走開；一條品系常同時標好幾型，只標一型就顯著的才算單型證據。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值；「該頁」指表格同一列的來源頁。

## 是什麼

**MBON-α2sc 是蕈狀體輸出神經元（[[e-mbon]]）的一型，樹突在 α 葉的 α2 區室。** 字尾 sc 的意思由 Aso 2014a 交代：三型 α/β KC 的軸突在葉裡同心排列成後層（p）、表層（s）、核心層（c），sc＝表層（surface）加核心層（core），表示它的樹突只取 α2 格裡表層與核心層 KC 的輸入；同一格的後層由另一型 MBON-α2p3p 取用（圖 12D、16F、16H）。同樣依 Aso 2014a：每半腦 1 顆、乙醯膽鹼性（推定），軸突雙側投射到 SIP、SLP 與背側側角（圖 16F）；舊名 MB-V2α（表 1，作者註明是「最可能的對應」），屬 V2 群。同一格送來多巴胺的是傳遞懲罰的 [[e-ppl1-alpha2alpha2]]。在本庫它出現在五篇：Aso 2014a 給它命名與形態；Aso 2014b 以 V2 群整群操作它；Hige 2015 用它示範「不同區室的誘發門檻不同」；Felsenberg 2017 把它算在消退所需的 V2 群裡；Huang 2024 量它的放電，並放進九神經元模型當 α2 模組的輸出。區室見 [[c-mb-compartment]]。

## 版本與規模（標記它的品系）

| 品系 | 來源 | 說明 |
|---|---|---|
| MB549C、MB080C、MB050B（split-GAL4） | Aso 2014a 表 1 | 表 1 列為這一型的品系；Aso 2014b 表 2 顯示 MB549C 另標 MBON-α′3ap、MB050B 另標 MBON-α′1，都不是只標它一型 |
| MB052B | Aso 2014b 表 2 | 它、MBON-α′3ap、MBON-α′1，另弱標 MBON-α2p3p、MBON-α′3m（V2 群整群）；在雄蠅另有雄性專一的表現 |
| R34B02-LexA | Aso 2014a 圖 11（標 α2 格的 MBON）；Hige 2015 | 讓它帶 GFP，方便電極對準 |
| MB052B | Felsenberg 2017 延伸圖 6j | V2 群五型一起（含它），用於阻斷 |
| R71D08-LexA | Felsenberg 2017 延伸圖 6m | V2 群其中三型（α2sc、α′3ap、α′3m），用於光活化 |
| R65B09-LexA | Felsenberg 2017 延伸圖 6l | V2 群五型加 α′2，用於光活化 |
| split-GAL4（品系名未印出） | Huang 2024 | 電壓成像；各型品系對照在延伸表 1，PDF 只有表題（？待查） |

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-aso-2014-mb-architecture]] | 命名與形態的原始出處（表 1、圖 12D、16F） | 每半腦 1 顆、乙醯膽鹼性（推定）；「一個區室被兩型 MBON 依層分掉」的例子：它讀到的 KC 不含後層（α/βp） |
| [[s-aso-2014-mbon-valence]] | 只以 V2 群的一員被操作：MB052B（五型）、MB549C（它＋α′3ap）、MB050B（它＋α′1）；CsChrimson 光遺傳活化、shibire^ts 阻斷 | MB052B 整群活化 → 推動靠近（\*\*\*）；只標子集的品系都不顯著。只在測驗時以 MB052B 阻斷，24 小時長期嫌惡記憶幾乎消失，五條只標其子集的品系都不顯著，作者因此說 V2 群「整群」負責讀出。MB050B 在 2 小時獎賞記憶顯著，但標得更多的 MB052B 不顯著，作者列為「未解決」 |
| [[s-hige-2015-heterosynaptic-plasticity]] | 活體全細胞記錄；MB099C 驅動 CsChrimson 活化 α2 一帶的 PPL1（含 PPL1-α′2α2），氣味配光（圖 6） | 1 秒氣味配 4 下光：無效（n＝7，OCT 約 84 → 76）；60 秒氣味配 120 下光：CS+ 約 74 → 5、CS− 約 66 → 58，只有 CS+ 顯著（n＝6）（※ 從圖判讀）。γ1pedc 用 1 下光就夠，所以 α2 的誘發門檻較高（相差超過 4 倍，上限未知） |
| [[s-felsenberg-2017-re-evaluation]] | 以 V2 群的一員被阻斷（MB052B）或光活化（R71D08-LexA 等） | 阻斷 V2 群擋住糖獎賞記憶的部分消退；活化 V2 群讓 PPL1 的鈣有反應（方向不一）；訓練後 V2 群對 CS+、CS− 的反應與假訓練組無差異。都是群體層級，不能單獨歸給它 |
| [[s-huang-2024-dopamine-memory-dynamics]] | 頭固定、腳踩小球的活果蠅上以電壓成像量放電；模型中的 Mα2 | 自發約 11 次／s，六型 MBON 中最低（※ 從圖判讀）；在 11 型神經元對五種氣味的反應相關矩陣中，只有它那一列像 DAN（圖 2j）。模型：一個訓練回合後它出現較持久、正負號依氣味先天價值而定的可塑性；拿掉 MBON-γ1pedc>α/β 的回饋，它的可塑性完全消失；它到 PPL1-α3 的興奮性回饋擬合出來近乎為 0 |

數值見各來源頁與 [[numbers]]。

## 已知的問題

- **Hige 2015 的「門檻較高」有活化強度的混淆。** α2 用 MB099C（多型 DAN，幾型兩篇說法不同，見 [[syn-contradictions]] 1.4），γ1pedc 用 MB320C（一顆）；兩種協定也同時改了氣味時長與光脈衝數。量到的是誘發門檻不同，不是規則形式不同。
- **Aso 2014b 也只有整群的證據。** 「V2 群推動靠近」「V2 群負責長期記憶的讀出」都來自 MB052B 一條同時標五型的品系；本庫沒有任何來源只活化或只阻斷它一型。
- **Felsenberg 2017 的操作是整群的。** 阻斷用的五型與活化用的三型不完全相同，「V2 中哪幾型影響 PPL1」無法從該篇確定。
- **Huang 2024 關於它的結論多半來自模型。** 它的實測只有自發放電與氣味反應；「可塑性依先天價值決定正負」「沒有回饋就沒有可塑性」都是擬合後模型的輸出，原文承認 α2 的結果與前人報告不一致。圖 1a 畫了它回到 DAN 的回饋線，不等於模型裡這條線有作用。
- **三篇的讀數不同。** Hige 是電極量的放電數，Huang 是電壓成像偵測的放電（MBON 偵測錯誤率最高每秒 1.7 次，對自發只有約 11 次的它不可忽略），Felsenberg 是鈣成像；數值不能並排。

## 相關

- 同格 DAN：[[e-ppl1-alpha2alpha2]]；同模型的 DAN：[[e-ppl1-alpha3]]；上游回饋：[[e-mbon-gamma1pedc]]
- 細胞：[[e-mbon]]、[[e-dopaminergic-neuron]]
- 品系與工具：[[e-split-gal4]]、[[e-mb099c]]、[[e-cschrimson]]、[[e-shibire-ts]]
- 概念：[[c-mb-compartment]]、[[c-kc-mbon-plasticity]]、[[c-memory-extinction]]、[[c-whole-cell-patch-clamp]]
- 主題：[[t-dopamine-to-plasticity]]、[[t-mbon-dan-feedback]]、[[t-memory-updating]]、[[t-mbon-to-action]]
- 來源：[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-felsenberg-2017-re-evaluation]]、[[s-huang-2024-dopamine-memory-dynamics]]
- 待開頁面：`e-mbon-v2-cluster`
