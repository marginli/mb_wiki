---
title: PPL1-γ1pedc 多巴胺神經元（PPL1-γ1pedc, MB-MP1）
created: 2026-10-25
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# PPL1-γ1pedc 多巴胺神經元（PPL1-γ1pedc, MB-MP1）


**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蕈狀體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」（α、α′、β、β′、γ），每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、γ2、α1）；細胞以所在區室命名。見 [[e-mushroom-body]]、[[c-mb-compartment]]。
- **DAN、PAM、PPL1**：多巴胺神經元（dopaminergic neuron）送出代表懲罰或獎賞的多巴胺；PAM 群多傳遞獎賞，PPL1 群（Handler 2019 寫作 PPL）多傳遞懲罰。
- **MBON**：蕈狀體輸出神經元，接收 KC 的訊號、推動果蠅靠近或走開；學習改變的是 KC→MBON 突觸的強弱。
- **CS+／CS−、順向／逆向**：訓練時配了糖、電擊或 DAN 活化的氣味（CS+），與沒配的對照氣味（CS−）。順向配對＝氣味先、多巴胺後；逆向配對＝多巴胺先、氣味後。
- **PI（表現指數）、LI（學習指數）**：行為分數。一群果蠅在兩種氣味間選擇，換算成一個數；多數篇落在 −1 到 +1（Hige 2015 的刻度不同），0＝沒有偏好，正負號的意思各篇不同（見 [[c-performance-index]]）。
- **消退、再鞏固**：學會後再聞 CS+ 卻沒有糖或電擊，學到的反應減弱，叫消退（[[c-memory-extinction]]）；記憶被叫出來後暫時變得不穩定、再重新存好，叫再鞏固（[[c-memory-consolidation]]）。
- **驅動品系**：讓外加基因只在選定神經元表現的果蠅品系。GAL4 與 LexA 是兩套互不干擾的開關；split-GAL4 把 GAL4 拆成兩半（AD 與 DBD），兩半都在的細胞才有作用（[[e-split-gal4]]）。基因型寫「X/+」表示只帶一個品系的對照組。
- **活化與阻斷工具**：CsChrimson 照紅光讓神經元放電（[[e-cschrimson]]）；P2X2 遇到 ATP 讓神經元放電（[[e-p2x2]]）；shibire^ts1（shi）升溫時暫時關掉神經元的輸出（[[e-shibire-ts]]），全程維持低溫的「允許溫度對照」用來排除品系本身的效果。
- **讀數與製備**：ΔF/F0＝螢光相對刺激前基線的變化比例（0.5＝亮了 50%），以遇鈣變亮的 GCaMP 量神經元活動（[[e-gcamp]]）；離體＝把腦取出泡在養液裡做實驗（[[c-ex-vivo-explant]]），活體＝活果蠅固定後打開頭殼看。
- **電壓成像、放電率**：電壓成像（voltage imaging）是用會隨膜電壓變亮變暗的螢光蛋白（Huang 2024 用 pAce）、每秒拍 1,000 張，看得到每一次放電；放電率＝每秒放電幾次。和鈣成像不同，它看得到放電「減少」。
- **舊名與新名**：Aso 2014a（[[s-aso-2014-mb-architecture]]）以前，蕈狀體的細胞型多用 Tanaka 2008 的舊名（MB-MP1、MB-V2α 等），同一顆細胞在不同論文裡名字不同；Aso 2014a 改以所在區室命名，並在表 1 給出新舊名對照。
- **一氧化氮（NO）、TPM、TH 突變**：Aso 2019 發現部分 DAN 除了多巴胺還放出 NO（由 NOS 酵素合成），作用與多巴胺可以相反；TPM 是 RNA 定序的表現量單位；TH 突變背景＝不能合成多巴胺的果蠅，用來看 DAN 在沒有多巴胺時還能寫入什麼。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值；「text.txt 第 N 行」＝本庫保存的論文全文文字檔的行號；「該頁」指表格同一列的來源頁。

## 是什麼

**PPL1-γ1pedc 是一型傳遞懲罰的多巴胺神經元（DAN），把多巴胺送進蕈狀體的 γ1pedc 區室。** 名字分兩段：PPL1 是它所屬的 DAN 細胞群（以細胞體所在位置命名，這一群多傳遞懲罰）；γ1pedc 是它支配的區室，在 γ 葉最靠近根部的一格一帶（區室見 [[c-mb-compartment]]）。字尾 pedc 指柄遠端的核心部位（core of distal pedunculus，柄是 KC 軸突從萼部往前集成的一束）；依 [[s-aso-2014-mb-architecture]]，pedc 不算在 15 個區室裡，但有自己專屬的一型 MBON 與一型 DAN。舊名 MB-MP1：這個新舊名對照的原始出處是 Aso 2014a 表 1（寫「MB-MP1, MP」，作者註明是「最可能的對應」）；Mao 2009 把 MB-MP1 描述為支配「腳跟與柄末端」的 PPL1；Hige 2015、Felsenberg 2017、Burke 2012 的實驗用這個舊名。細胞數：Aso 2014a 表 1 記每半腦 1–2 顆，Aso 2019 寫每半球一顆。同一格裡接收 KC 訊號的輸出神經元是 [[e-mbon-gamma1pedc]]。**γ1 格不只它一型 DAN**：Aso 2014a 表 1 另列第六型 PPL1-γ1，稀疏支配 γ1，只在 TH-GAL4 的隨機標記中看過、做不出 split-GAL4（表 1 註腳）。本頁也收錄**專門標記它的品系 MB320C**：依 Hige 2015，MB320C「只標一顆 PPL1-γ1pedc 神經元」（text.txt 第 194–195 行）；左右腦是否各一顆，原文沒說：？待查。

## 版本與規模（標記它的品系）

| 品系 | 來源 | 說明 |
|---|---|---|
| **MB320C**（split-GAL4；TH-p65ADZp／22B12-ZpGAL4DBD） | Hige 2015 自述「we created」；Aso 2016 圖 1C 圖說把其影像指向 Aso et al. 2014a；Aso 2014b 圖 6K 已用它標這一型做雙色標記；Aso 2019 圖 6D | 只標這一型 |
| MB438B（split-GAL4；AD R30E11／DBD R22B12） | Aso 2014a 表 1 列為這一型的品系；Aso 2014b 用於阻斷與熱活化 | 依 Aso 2014b 表 2：標這一型，**另弱標 PPL1-α2α′2**（括號＝弱、隨機或只在部分報導基因下可見） |
| VT045661-LexA | Aso 2016 圖 4A；Aso 2019 圖 6B、6C 與 TH 突變組 | 另一套表現系統，用來與 α1 的 DAN 同時活化（Aso 2016）、在 TH 突變背景下活化（Aso 2019） |
| c061-GAL4;MBGAL80 | Burke 2012；Felsenberg 2017 延伸圖 6f | 用於阻斷 MB-MP1 或在其中表現 RNAi |
| MB504B、TH-GAL4 | Felsenberg 2017 延伸圖 6b–c；Hige 2015；Huang 2024 圖 1b（MB504B 同時標它與 PPL1-γ2α′1、-α′2α2）；Mao 2009、Dylla 2017（TH-GAL4） | 涵蓋它的較廣品系（見 [[e-mb504b]]、[[e-th-gal4]]）；TH-GAL4 也標到同樣支配 γ1 的 PPL1-γ1 |

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-mao-2009-dopaminergic-neuron-types]] | TH-GAL4 的 flip-out 單細胞選殖，描述為「腳跟與柄末端」型，並對到 Tanaka 2008 的舊名 MB-MP1 | 14 個樣本；左右兩側對稱支配腳跟與柄末端。**沒有功能資料**（鈣成像只做了垂直葉四段）。對到新名靠 Felsenberg 2017 或 Aso 2014a 表 1 的舊名對照串接 |
| [[s-burke-2012-octopamine-dopamine-reward]] | 以 c061-GAL4;MBGAL80 在 MB-MP1（該篇的寫法）表現 *octβ2R* RNAi 或 shi^ts1，同時以 Tdc2-LexA 活化章魚胺神經元；GRASP 看兩者接觸 | 兩種操作都讓章魚胺造出的人工**獎賞**記憶形不成；GRASP 在 ampr 有強訊號、另在蕈狀體腳跟有訊號。作者的解釋：MB-MP1 被人工活化時提供嫌惡增強（引 Aso 2010），章魚胺必須經 Octβ2R 調節它。**章魚胺讓它的活動往哪個方向變，該篇沒有量** |
| [[s-aso-2014-mb-architecture]] | 命名與形態的原始出處：對位到標準腦的影像、表 1 的品系與舊名對照 | 每半腦 1–2 顆；表 1 品系 MB438B，舊名 MB-MP1、MP；末梢與 MBON-γ1pedc>α/β 的樹突重疊（圖 15F）；γ1 另有第六型 PPL1-γ1（無品系） |
| [[s-aso-2014-mbon-valence]] | shi^ts 阻斷（MB438B）；dTrpA1 熱活化代替電擊；MCFO 單細胞形態；與 MBON 雙色標記（MB320C／R12G04-LexA） | 阻斷 → 2 小時嫌惡氣味記憶與嫌惡顏色記憶都受損；熱活化代替電擊 → 3 分鐘記憶約 −0.53（對照約 0，※ 從圖判讀）；末梢與 MBON-γ1pedc>α/β 的樹突在 γ1 與 pedc 精確重疊（圖 6K）。MB438B 也弱標 PPL1-α2α′2，效果可能部分來自那一型 |
| [[s-hige-2015-heterosynaptic-plasticity]] | MB320C 驅動 CsChrimson，氣味配光，活體記錄 MBON-γ1pedc；行為上以光代替電擊 | 配對氣味的放電降 80% ± 5.7%、電荷降 90% ± 3.7%；逆向配對無效；學會迴避並類化到相似氣味 |
| [[s-aso-2016-dan-cell-type-rules]] | MB320C 驅動 CsChrimson，十個時間差的行為掃描與多種更新協定 | 光在氣味開始後 0–20 s → 嫌惡（PI 最低約 −0.45）；早 20–60 s → 喜好（約 +0.15）；學得快、1 天後幾乎消失、未配對 DAN 活化削弱記憶最多、只記得最後一組配對 |
| [[s-felsenberg-2017-re-evaluation]] | c061-GAL4;MBGAL80 驅動 shi^ts1 阻斷；在體成像它對氣味的反應 | 單獨阻斷不影響糖獎賞記憶的消退（延伸圖 3c）；訓練後對 CS+、CS− 的反應與假訓練無差異（延伸圖 4f） |
| [[s-dylla-2017-trace-conditioning-dan-plasticity]] | TH-GAL4 鈣成像 γ1 區的 DAN；痕跡制約（氣味與電擊之間隔一段空檔） | γ1 區混有 1–2 顆 PPL1-γ1pedc 與 1 顆 PPL1-γ1，**不是單一型的資料**。電擊反應強（約 0.87，同區 BUT 約 0.56，※ 從圖判讀）；訓練後對 CS 的反應比不配對組大 0.27（正規化 ΔF/F，整段訓練期 p < 0.001），且配對組自己也顯著升高 |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | VT045661-LexA（圖 6B、6C 與 TH 突變組）與 MB320C（圖 6D）驅動 CsChrimson，以紅光代替懲罰；在它裡面以 RNAi 壓低一氧化氮合成酶（NOS） | **它表現 NOS1（22 TPM，受檢細胞型中最高）**。TH 突變（不能合成多巴胺）背景下活化它造出正價性記憶（價性反轉），要 1×1 分鐘以上的訓練、10 分鐘才顯現；正常背景壓低 NOS：即時記憶不變，3 小時與 6 小時的負價性記憶顯著變強；10 次間隔訓練後出現原本沒有的一日記憶（圖 6E 的品系圖說未寫，見該頁） |
| [[s-huang-2024-dopamine-memory-dynamics]] | 電壓成像量它在頭固定、腳踩小球的活果蠅上的單次放電；模型中的 Dγ1（短期記憶模組 γ1 的 DAN） | 自發約 20 次／s；單下電擊（20 V、0.2 s）時約 22 → 50 次／s、最高點約 60；吃糖約 17 → 13（皆 ※ 從圖判讀）；吸引氣味讓它放電下降；氣味加 5 下電擊約等於兩者分別給的相加（延伸圖 8d–g，14 隻）。6 回合訓練後 CS+ 對 CS− 的偏差全程不顯著——這一型自己沒有「學到」CS+ |

數值見各來源頁與 [[numbers]]。Felsenberg 2018 只經由 MB504B（含這一型在內的四型 PPL1）阻斷，沒有單獨操作它，不列入表。

## 已知的問題

- **逆向配對：突觸不變，行為卻能反轉。** Hige 2015 的逆向（光比氣味早約 2.0–0.5 s）突觸不變；Aso 2016 在早 10 s 也無效，早 20–60 s 才出現喜好。兩者都不是在同一條件下同時量突觸與行為；與 Handler 2019 的 γ4 結果並列見 [[syn-contradictions]] 1.1。
- **「一顆」只是品系的描述。** Hige 的單顆標記影像在補充圖 S1A：？待查。Aso 2016 圖 4A 改用 VT045661-LexA，兩種品系的表現量是否相近，該篇沒比較。
- **單獨阻斷無效不等於不參與。** Felsenberg 2017 中 MB504B（四型一起）阻斷能部分擋住消退，個別型別阻斷都不能；正文推測 CS+ 會優先活化 MB-MP1，由它參與寫下消退記憶；但該篇以 MB504B 成像的三顆 PPL1 細胞沒有指認各是哪一型，這個推測在成像資料中找不到依據（見 [[s-felsenberg-2017-re-evaluation]]）。
- **行為與生理不是同一批果蠅。** Hige 2015 的突觸與行為用不同光協定；Aso 2016 全是行為；Huang 2024 的成像與小球行為也是分開的兩批果蠅（成像用的藍光干擾行為）。
- **Huang 2024 的模型規則與 Hige 2015 在這一格牴觸。** Huang 的模型假設「DAN 比氣味先到或被抑制時，KC→MBON 變強」，並用在 γ1 模組；Hige 2015 在 γ1pedc 讓光比氣味早約 2.0 s，突觸完全不變。⚠️ 矛盾｜未裁決，見 [[syn-contradictions]] 1.9。
- **它不是只放多巴胺。** Aso 2019 證明它同時以一氧化氮（NO）為共同傳遞物，NO 的作用與多巴胺相反、較慢。凡是用它做「多巴胺訊號」的實驗（本庫 Hige 2015、Aso 2016、Huang 2024），結果都含有 NO 的成分；短訓練下 NO 幾乎還沒作用（Aso 2019 圖 6B），長訓練與長時距下則不能忽略。
- **廣泛品系動到的不只它一型。** γ1 格另有一型 PPL1-γ1（Aso 2014a 表 1，無專屬品系），TH-GAL4 兩型都標；Dylla 2017 的 γ1 區訊號就是兩型混在一起。用 TH-GAL4 或 c061-GAL4;MBGAL80 這類品系「活化／阻斷 γ1pedc 的 DAN」時，可能同時動到 PPL1-γ1。Aso 2014b 的阻斷品系 MB438B 另弱標 PPL1-α2α′2。
- **它出現在獎賞迴路裡，是被調節的對象。** Burke 2012 是本庫唯一讓它出現在獎賞記憶裡的來源；該篇自己的解釋與「它傳遞懲罰」不牴觸，引用時要寫清楚它是被章魚胺調節的對象，不是獎賞的傳遞者。
- **放電率要註明條件。** Huang 2024 的電擊是 20 V、每下 0.2 s，比 T 迷宮慣用的 60–90 V、1.25 s 弱得多；基線也隨時間窗不同（圖 1d 約 20、圖 2d 約 22、圖 2e 約 17，※ 從圖判讀）。不能把這組數字直接當成 T 迷宮電擊下的放電率。

## 相關

- 同格輸出：[[e-mbon-gamma1pedc]]；同群其他型：[[e-ppl1-gamma2alpha1]]、[[e-ppl1-alpha2alpha2]]、[[e-ppl1-alpha3]]；細胞群：[[e-dopaminergic-neuron]]
- 品系：[[e-split-gal4]]、[[e-mb504b]]、[[e-mb099c]]、[[e-th-gal4]]；工具：[[e-cschrimson]]、[[e-shibire-ts]]、`e-dtrpa1`、[[e-mcfo]]、[[e-grasp]]
- 概念：[[c-cs-us-timing]]、[[c-kc-mbon-plasticity]]、[[c-us-substitution]]
- 主題：[[t-timing-rules]]、[[t-memory-updating]]；矛盾：[[syn-contradictions]]
- 來源：[[s-mao-2009-dopaminergic-neuron-types]]、[[s-burke-2012-octopamine-dopamine-reward]]、[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-felsenberg-2017-re-evaluation]]、[[s-dylla-2017-trace-conditioning-dan-plasticity]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-huang-2024-dopamine-memory-dynamics]]
