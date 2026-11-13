---
title: PPL1-γ2α′1 多巴胺神經元（PPL1-γ2α′1, MB-MV1）
created: 2026-10-25
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# PPL1-γ2α′1 多巴胺神經元（PPL1-γ2α′1, MB-MV1）


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
- **電壓成像、放電率**：電壓成像（voltage imaging）是用會隨膜電壓變亮變暗的螢光蛋白（Huang 2024 用 pAce）、每秒拍 1,000 張，看得到每一次放電；放電率＝每秒放電幾次。
- **舊名與新名**：Aso 2014a（[[s-aso-2014-mb-architecture]]）以前，蕈狀體的細胞型多用 Tanaka 2008 的舊名（MB-MP1、MB-V2α 等），同一顆細胞在不同論文裡名字不同；Aso 2014a 改以所在區室命名，並在表 1 給出新舊名對照。
- **一氧化氮（NO）、TPM、TH 突變**：Aso 2019 發現部分 DAN 除了多巴胺還放出 NO（由 NOS 酵素合成），作用與多巴胺可以相反；TPM 是 RNA 定序的表現量單位；TH 突變背景＝不能合成多巴胺的果蠅，用來看 DAN 在沒有多巴胺時還能寫入什麼。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值；「text.txt 第 N 行」＝本庫保存的論文全文文字檔的行號；「該頁」指表格同一列的來源頁。

## 是什麼

**PPL1-γ2α′1 是 PPL1 群（多傳遞懲罰）中的一型多巴胺神經元（DAN），軸突同時伸進蕈狀體的 γ2 與 α′1 兩個區室。** 名字裡串兩段區室名，就表示它跨這兩格；Hige 2015 的描述是「投射到相鄰的 γ2 區室（也投射到 α′1）」。舊名 MB-MV1：新舊名對照的原始出處是 Aso 2014a 表 1（作者註明是「最可能的對應」），Felsenberg 2017 也列出這個對照；Mao 2009 把 MB-MV1 描述為支配垂直葉「下段與交界」的 PPL1。Aso 2014a 表 1 記每半腦 1 顆。同一格的輸出神經元是 [[e-mbon-gamma2alpha1]]。區室見 [[c-mb-compartment]]。

## 版本與規模（標記它的品系）

| 品系 | 來源 | 標到什麼 |
|---|---|---|
| MB296B、MB439B（split-GAL4） | Aso 2014a 表 1 | 表 1 列為這一型的品系 |
| MB296B-GAL4、R73F07-GAL4 | Felsenberg 2017 延伸圖 6d–e | 只標 PPL1-γ2α′1 |
| 73F07-LexA | Handler 2019 | 基因型表標「γ2 DANs」 |
| MB099C（TH／73F07 兩半） | Hige 2015、Aso 2016 | 含它在內的兩型或四型 PPL1（見 [[e-mb099c]]） |
| TH-GAL4 | Mao 2009、Dylla 2017 | 群體品系；兩篇的 γ2（下段連交界）訊號依解剖歸給這一型（見 [[e-th-gal4]]） |
| MB504B | Felsenberg 2017 延伸圖 6c；Huang 2024 圖 1b | 含它在內的四型 PPL1（Felsenberg 2017）；Huang 2024 圖 1b 指出其中三型：它、PPL1-γ1pedc、-α′2α2（見 [[e-mb504b]]） |

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-mao-2009-dopaminergic-neuron-types]] | TH-GAL4 的 flip-out 單細胞選殖，描述為「下段與交界」型並對到舊名 MB-MV1；TH-GAL4 > G-CaMP 在「下段連交界」成像 | 13 個樣本。鈣反應：電擊 0.01 mA 約 74%（四段最強；0.001 mA 約 41%）、MCH 約 22%；一分鐘配對後 10 分鐘，五組都沒有顯著改變（皆 ※ 從圖判讀）。ROI 是群體品系的訊號，屬於這一型是依解剖推定 |
| [[s-aso-2014-mb-architecture]] | 命名與形態的原始出處（表 1、圖 16C） | 每半腦 1 顆；表 1 品系 MB296B、MB439B，舊名 MB-MV1 |
| [[s-felsenberg-2017-re-evaluation]] | MB296B（另以 R73F07 重做）驅動 shi^ts1 阻斷；離體以光活化 γ2α′1 MBON，量它的鈣 | 再聞 CS− 時阻斷 → 6 h 獎賞記憶消失（再鞏固失敗）；聞完才阻斷、只在提取時阻斷都不顯著；γ2α′1 MBON 活化後 ΔF/F₀ 約 0.03 → 0.72（4 筆，※ 從圖判讀） |
| [[s-dylla-2017-trace-conditioning-dan-plasticity]] | TH-GAL4 鈣成像 γ2 區的 DAN（該篇說 γ2 與 α′1 只由這一顆 DAN 支配）；痕跡制約 | 電擊反應全區最強（約 1.10，同區 BUT 約 0.88，※ 從圖判讀）；訓練後對 CS 比不配對組大 0.30（整段訓練期 p < 0.05），但配對組本身略低於訓練前，差值主要來自不配對組下降（約 −0.05 vs −0.35，※ 從圖判讀） |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | TH 突變（不能合成多巴胺）背景下以光活化（圖 2）；餵 NOS 抑制劑 L-NNA；異位表現 NOS | **沒有價性反轉**：有無多巴胺都造出負價性記憶（約 −0.30 與 −0.22，※ 從圖判讀），L-NNA 不影響 → 作者推論它帶有一種與多巴胺同向、尚未鑑定的共同傳遞物。NOS1 僅約 1 TPM。異位表現 NOS 後出現價性反轉（圖 4 補充圖 1，本庫未取得） |
| [[s-handler-2019-dopamine-receptor-timing]] | 73F07-LexA 驅動 P2X2，離體活化「γ2 DAN」並量 γ2 MBON | 補充圖 S3D：？待查（補充資料未取得） |
| [[s-hige-2015-heterosynaptic-plasticity]] | 經 MB099C 與其他型一起活化 | 氣味配光後，鄰格的 MBON-γ1pedc 不變（多巴胺不越界的證據之一） |
| [[s-aso-2016-dan-cell-type-rules]] | 經 MB099C 與 PPL1-α′2α2 一起活化 | 10 次間隔訓練後有 4 日記憶（圖 2C）；作者推測 PPL1-γ2α′1 可能經由促進學習後的睡眠而廣泛幫助記憶鞏固（text.txt 第 374–378 行，未檢驗） |
| [[s-huang-2024-dopamine-memory-dynamics]] | 電壓成像量它在頭固定、腳踩小球的活果蠅上的單次放電；不在九神經元模型內 | 自發約 12 次／s；單下電擊（20 V、0.2 s）約 13 → 43 次／s、最高點約 50；吃糖約 16 → 8（皆 ※ 從圖判讀）；6 回合訓練前後對 CS+、CS− 的反應都不變。作者在延伸圖 13i 寫它受果蠅的運動調節；摘要把它與 PPL1-γ1pedc 並列為控制短期記憶形成的兩型 |

數值見各來源頁與 [[numbers]]。

## 已知的問題

- **Handler 的「γ2 DAN」是不是這一型。** ※ 推論：Felsenberg 2017 說 R73F07-GAL4 只標 PPL1-γ2α′1，Handler 用 73F07-LexA 標「γ2 DAN」，兩者可能是同一型；但 GAL4 與 LexA 版本標到的範圍不一定相同，兩篇沒有比對：？待查。Cohn 2015 也活化「γ2 DAN」（圖 6C、6E），品系名主文沒寫，是否同一型無從判斷。
- **單獨操作它的只有 Felsenberg 2017（阻斷）與 Aso 2019（在七個驅動品系逐一光活化的實驗中，有它單獨的一組）。** Hige 2015 與 Aso 2016 都經由 MB099C 和其他型一起活化，結果不能歸給這一型。Huang 2024 單獨**量**了它的放電，但沒有操作它。
- **懲罰型 DAN 為何保住獎賞記憶，Felsenberg 2017 沒有解釋。** γ2α′1 MBON 與這型 DAN 的連結，證據只有離體實驗（光活化 MBON、量這型 DAN 的鈣），沒有氣味、n 小，不能說明兩者之間是直接突觸。
- **Dylla 2017 的「增強」主要是相對量。** 配對組沒有升高，是不配對組下降；不配對組的下降可能來自重複聞同一氣味的疲乏或螢光漂白（該篇自己列出的解釋）。
- **它的第二種傳遞物還不知道是什麼。** Aso 2019 只從「沒有多巴胺仍能寫入負價性記憶」推論它存在。
- **MB099C 的組成兩篇不同**，見 [[syn-contradictions]] 1.4。

## 相關

- 同格輸出：[[e-mbon-gamma2alpha1]]；同群其他型：[[e-ppl1-gamma1pedc]]、[[e-ppl1-alpha2alpha2]]、[[e-ppl1-alpha3]]；細胞群：[[e-dopaminergic-neuron]]
- 品系：[[e-mb099c]]、[[e-mb504b]]、[[e-split-gal4]]、[[e-th-gal4]]；工具：[[e-shibire-ts]]、[[e-p2x2]]
- 概念：[[c-memory-consolidation]]、[[c-ex-vivo-explant]]
- 主題：[[t-memory-updating]]、[[t-mbon-dan-feedback]]；矛盾：[[syn-contradictions]]
- 來源：[[s-mao-2009-dopaminergic-neuron-types]]、[[s-aso-2014-mb-architecture]]、[[s-dylla-2017-trace-conditioning-dan-plasticity]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-felsenberg-2017-re-evaluation]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-huang-2024-dopamine-memory-dynamics]]
