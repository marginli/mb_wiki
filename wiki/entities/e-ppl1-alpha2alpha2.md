---
title: PPL1-α′2α2 多巴胺神經元（PPL1-α′2α2, MB-V1）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# PPL1-α′2α2 多巴胺神經元（PPL1-α′2α2, MB-V1）


**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蕈狀體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」（α、α′、β、β′、γ），每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、α′2、α2）；細胞以所在區室命名。見 [[e-mushroom-body]]、[[c-mb-compartment]]。
- **DAN、PAM、PPL1**：多巴胺神經元（dopaminergic neuron）送出代表懲罰或獎賞的多巴胺；PAM 群多傳遞獎賞，PPL1 群多傳遞懲罰（見 [[e-dopaminergic-neuron]]）。
- **MBON**：蕈狀體輸出神經元，接收 KC 的訊號、推動果蠅靠近或走開；學習改變的是 KC→MBON 突觸的強弱（見 [[e-mbon]]）。
- **CS+／CS−**：訓練時配了電擊、糖或 DAN 活化的氣味（CS+），與沒配的對照氣味（CS−）。
- **驅動品系**：讓外加基因只在選定神經元表現的果蠅品系；split-GAL4 把 GAL4 拆成兩半，兩半都在的細胞才有作用（[[e-split-gal4]]）。GAL4 與 LexA 是兩套互不干擾的開關。
- **工具**：CsChrimson 照紅光讓神經元放電（[[e-cschrimson]]）；shibire^ts1 升溫時暫時關掉神經元的輸出（[[e-shibire-ts]]）。
- **電壓成像、放電率**：電壓成像（voltage imaging）用會隨膜電壓變亮變暗的螢光蛋白（Huang 2024 用 pAce）、每秒拍 1,000 張，看得到每一次放電；放電率＝每秒放電幾次。鈣成像（[[e-gcamp]]）看的是細胞內鈣，放電減少時不易看出。
- **偏差（bias）**：Huang 2024 的讀數，(CS+ 引起的放電改變 − CS− 引起的放電改變) 減去訓練前的同一值，單位每秒放電次數。
- **舊名與新名**：Aso 2014a（[[s-aso-2014-mb-architecture]]）以前，蕈狀體的細胞型多用 Tanaka 2008 的舊名（MB-MP1、MB-V2α 等），同一顆細胞在不同論文裡名字不同；Aso 2014a 改以所在區室命名，並在表 1 給出新舊名對照。
- **一氧化氮（NO）、TPM、TH 突變**：Aso 2019 發現部分 DAN 除了多巴胺還放出 NO（由 NOS 酵素合成），作用與多巴胺可以相反；TPM 是 RNA 定序的表現量單位；TH 突變背景＝不能合成多巴胺的果蠅，用來看 DAN 在沒有多巴胺時還能寫入什麼。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值；「該頁」指表格同一列的來源頁。

## 是什麼

**PPL1-α′2α2 是 PPL1 群（多傳遞懲罰）中的一型多巴胺神經元（DAN），軸突伸進蕈狀體的 α′2 與 α2 兩個區室。** 舊名 MB-V1：新舊名對照的原始出處是 Aso 2014a 表 1（作者註明是「最可能的對應」），Felsenberg 2017 也列出這個對照；Mao 2009 把 MB-V1 描述為支配垂直葉「上段」的 PPL1。Aso 2014a 表 1 記每半腦 1 顆，並以它為「一型 DAN 支配兩格」的例子：它支配的 α′2 與 α2 這塊區域由三型 MBON（MBON-α′2、[[e-mbon-alpha2sc]]、MBON-α2p3p）覆蓋（圖 12D；形態見圖 16I）。Aso 2014b 表 2 把同一型寫作 PPL1-α2α′2。α2 格讀取 KC 訊號的輸出神經元之一是 [[e-mbon-alpha2sc]]。本庫沒有任何一篇用只標它一型的品系去操作它：Hige 2015 與 Aso 2016 經由 MB099C 和其他型一起活化，Felsenberg 2017 用 MB058B 阻斷，Huang 2024 只量它的放電。區室見 [[c-mb-compartment]]。

## 版本與規模（標記它的品系）

| 品系 | 來源 | 說明 |
|---|---|---|
| MB058B | Aso 2014a 表 1；Felsenberg 2017 延伸圖 3 | 表 1 列為這一型的品系；Felsenberg 用於阻斷 MB-V1 |
| MB438B | Aso 2014b 表 2 | 主要標 PPL1-γ1pedc，**弱標**這一型（寫作 PPL1-α2α′2）；Aso 2014b 用它阻斷 PPL1-γ1pedc 時可能也動到這一型 |
| TH-GAL4 | Mao 2009 | 群體品系；「上段」的訊號依解剖歸給這一型（見 [[e-th-gal4]]） |
| R82C10-LexA | Huang 2024 延伸圖 13 | 驅動 jGCaMP7b 做這一型的鈣成像；電壓成像用的 split-GAL4 品系在延伸表 1，未印出（？待查） |
| MB099C | Hige 2015、Aso 2016 | 含它在內的兩型或四型 PPL1（兩篇說法不同，見 [[e-mb099c]]、[[syn-contradictions]] 1.4）；兩種說法都含它 |
| MB504B | Felsenberg 2017 延伸圖 6c；Huang 2024 圖 1b | 含它在內的多型 PPL1；Huang 圖 1b 點名它與 PPL1-γ1pedc、-γ2α′1（見 [[e-mb504b]]） |

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-mao-2009-dopaminergic-neuron-types]] | TH-GAL4 的 flip-out 單細胞選殖，描述為「上段」型並對到舊名 MB-V1；TH-GAL4 > G-CaMP 在「上段」成像 | 5 個樣本。鈣反應：電擊（0.01 mA）約 6%（四段最弱）、MCH 約 19%、OCT 隨濃度上升至約 21%；一分鐘配對後 10 分鐘對 OCT 的反應（後測／前測）：未處理 96%、順向 24%、逆向 39%、只氣味 55%、只電擊 95%，順向、逆向、只氣味彼此無差異——沒有專屬於配對的改變（皆 ※ 從圖判讀）。電擊反應弱，與 Huang 2024「電擊不顯著」方向一致 |
| [[s-aso-2014-mb-architecture]] | 命名與形態的原始出處（表 1、圖 12D、16I） | 每半腦 1 顆；表 1 品系 MB058B，舊名 MB-V1 |
| [[s-hige-2015-heterosynaptic-plasticity]] | 經 MB099C 驅動 CsChrimson 與其他型一起活化，記錄 α2 格的 MBON-α2sc；補充圖 S2B 確認光脈衝能讓它放電 | 1 秒氣味配 4 下光無效；60 秒氣味配 120 下光才讓 CS+ 放電大降（見 [[e-mbon-alpha2sc]]）。作者據此說 α2 的誘發門檻比 γ1pedc 高，並承認「PPL1-α′2α2 可能在不同刺激條件下誘發可塑性」 |
| [[s-aso-2016-dan-cell-type-rules]] | 經 MB099C（該篇說是它加 PPL1-γ2α′1 兩型）驅動 CsChrimson，以紅光代替電擊 | 間隔訓練 10 次後有 4 日記憶（圖 2C）；但結果不能單獨歸給它 |
| [[s-felsenberg-2017-re-evaluation]] | MB058B 驅動 shi^ts1，在糖獎賞記憶再聞 CS+ 時阻斷；活體鈣成像它對 CS+、CS− 的反應 | 單獨阻斷不影響消退（延伸圖 3）；糖獎賞訓練後 3 小時，它對 CS+、CS− 的反應與假訓練組無差異（延伸圖 4f） |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | 只在「PPL1 四型合一」的品系裡被一起活化（圖 1、圖 4C），從未單獨測試 | NOS1 約 8 TPM（受檢細胞型中第三高，僅次於 PPL1-γ1pedc 22 與 PAM-γ5 16）。**它會不會也有價性反轉，該篇沒有測** |
| [[s-huang-2024-dopamine-memory-dynamics]] | 頭固定、腳踩小球的活果蠅上以電壓成像量單次放電；模型中的 Dα2 | 自發約 10 次／s；單下電擊（20 V、0.2 s）的實驗中基線約 7、電擊時無顯著變化；吃糖約 11 → 8（皆 ※ 從圖判讀）。6 回合電擊訓練後，它對吸引氣味 CS+ 的反應由下降轉為上升（Mid、5 分鐘時偏差顯著），1 小時回到下降；作者把它與 PPL1-α3 並列為受 MBON-γ1pedc>α/β 抑制、回饋減弱後才編碼淨價值的兩型 |

數值見各來源頁與 [[numbers]]。

## 已知的問題

- **它可能也放一氧化氮，但沒人單獨測過。** NOS1 表現量排第三（Aso 2019），而該篇「NOS 高的就會價性反轉」的對應只在 γ1pedc 與 PAM-γ5 上檢驗過；四型合一品系的結果不能歸給它。
- **沒有單型操作的證據。** Hige 2015 與 Aso 2016 的活化都經由 MB099C，至少還有 PPL1-γ2α′1 一起動；Felsenberg 2017 的阻斷無效也不等於它不參與（該篇的 PPL1 群阻斷有效，個別型阻斷都無效）。
- **電擊時不放電，訓練後卻對 CS+ 放電。** Huang 2024 的單下電擊沒有讓它顯著增加放電，但訓練後它對 CS+ 的反應轉正；作者歸因於 MBON-γ1pedc>α/β 的回饋減弱。它在 Huang 模型中的角色（α2 模組）擬合出來近乎無作用，原文也承認 α2 的結果與前人報告不一致——圖上有連線、模型裡有作用、實驗上有因果，三者要分開讀。
- **鈣成像看不到它的放電下降。** Huang 2024 延伸圖 13a、c：R82C10-LexA 驅動的鈣訊號難以捕捉它對氣味的雙向編碼；而電壓成像用的是另一個品系，比較的是同型細胞、不是同一品系。Felsenberg 2017 延伸圖 4f 的「訓練後無差異」也是鈣成像。
- **Felsenberg 2017 延伸圖 4f 的品系名有誤。** 圖說把 MB-V1、MB-MP1 的品系寫成 MB052B-GAL4，而 MB052B 依該篇延伸圖 6j 標的是 V2 群 MBON（單篇自身不一致，⚠️）。
- **MB099C 的組成未定**，見 [[syn-contradictions]] 1.4。

## 相關

- 同群其他型：[[e-ppl1-gamma1pedc]]、[[e-ppl1-gamma2alpha1]]、[[e-ppl1-alpha3]]；細胞群：[[e-dopaminergic-neuron]]
- 同格輸出：[[e-mbon-alpha2sc]]；上游回饋：[[e-mbon-gamma1pedc]]
- 品系：[[e-split-gal4]]、[[e-mb099c]]、[[e-mb504b]]；工具：[[e-cschrimson]]、[[e-shibire-ts]]、[[e-gcamp]]
- 概念：[[c-mb-compartment]]、[[c-kc-mbon-plasticity]]、[[c-memory-extinction]]
- 主題：[[t-mbon-dan-feedback]]、[[t-dopamine-to-plasticity]]；矛盾：[[syn-contradictions]]
- 來源：[[s-mao-2009-dopaminergic-neuron-types]]、[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-felsenberg-2017-re-evaluation]]、[[s-huang-2024-dopamine-memory-dynamics]]
