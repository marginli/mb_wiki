---
title: γ4 輸出神經元（γ4 MBON）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-learning]
confidence: medium
---

# γ4 輸出神經元（γ4 MBON）


**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蘑菇體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」（α、α′、β、β′、γ），每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、γ2、α1）；細胞以所在區室命名。見 [[e-mushroom-body]]、[[c-mb-compartment]]。
- **DAN、PAM、PPL1**：多巴胺神經元（dopaminergic neuron）送出代表懲罰或獎賞的多巴胺；PAM 群多傳遞獎賞，PPL1 群（Handler 2019 寫作 PPL）多傳遞懲罰。
- **MBON**：蘑菇體輸出神經元，接收 KC 的訊號、推動果蠅靠近或走開；學習改變的是 KC→MBON 突觸的強弱。
- **CS+／CS−、順向／逆向**：訓練時配了糖、電擊或 DAN 活化的氣味（CS+），與沒配的對照氣味（CS−）。順向配對＝氣味先、多巴胺後；逆向配對＝多巴胺先、氣味後。
- **PI（表現指數）、LI（學習指數）**：行為分數。一群果蠅在兩種氣味間選擇，換算成一個數；多數篇落在 −1 到 +1（Hige 2015 的刻度不同），0＝沒有偏好，正負號的意思各篇不同（見 [[c-performance-index]]）。
- **消退、再鞏固**：學會後再聞 CS+ 卻沒有糖或電擊，學到的反應減弱，叫消退（[[c-memory-extinction]]）；記憶被叫出來後暫時變得不穩定、再重新存好，叫再鞏固（[[c-memory-consolidation]]）。
- **驅動品系**：讓外加基因只在選定神經元表現的果蠅品系。GAL4 與 LexA 是兩套互不干擾的開關；split-GAL4 把 GAL4 拆成兩半（AD 與 DBD），兩半都在的細胞才有作用（[[e-split-gal4]]）。基因型寫「X/+」表示只帶一個品系的對照組。
- **活化與阻斷工具**：CsChrimson 照紅光讓神經元放電（[[e-cschrimson]]）；P2X2 遇到 ATP 讓神經元放電（[[e-p2x2]]）；shibire^ts1（shi）升溫時暫時關掉神經元的輸出（[[e-shibire-ts]]），全程維持低溫的「允許溫度對照」用來排除品系本身的效果。
- **讀數與製備**：ΔF/F0＝螢光相對刺激前基線的變化比例（0.5＝亮了 50%），以遇鈣變亮的 GCaMP 量神經元活動（[[e-gcamp]]）；離體＝把腦取出泡在養液裡做實驗（[[c-ex-vivo-explant]]），活體＝活果蠅固定後打開頭殼看。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值；「text.txt 第 N 行」＝本庫保存的論文全文文字檔的行號；「該頁」指表格同一列的來源頁。

## 是什麼

樹突在 γ 葉第 4 格（γ4 區室）的蘑菇體輸出神經元（[[e-mbon]]）。γ 葉沿長度分 γ1–γ5 五格，每格有自己的 MBON 讀取 Kenyon 細胞（KC）的訊號，也有自己的多巴胺神經元（DAN）調整這個突觸（見 [[c-mb-compartment]]）。γ4 格的 DAN 屬於 PAM 群，以 58E02／R58E02 這段調控序列標記（見 [[e-r58e02]]）。庫內兩篇都只用區室名稱呼它（「γ4 MBON」），沒有給更完整的細胞名；兩篇出自同一實驗室（Ruta 實驗室），量的是 KC→γ4 MBON 突觸往哪個方向變。

## 版本與規模（標記它的品系）

| 來源 | 品系 |
|---|---|
| Cohn 2015 | 主文沒寫品系名（論文稱 MBON-specific drivers；？待查） |
| Handler 2019 | 離體 VT026001-Gal4；在體與閉迴路 R53C03-LexA |

※ 推論：兩篇的「γ4 MBON」是同一型細胞。依據：同一實驗室、同以區室命名、都用 58E02 標的 DAN 去調它；但 Cohn 沒寫品系，無法逐一比對。

## 庫內誰用了它

| 來源 | 怎麼用 | 看到什麼 |
|---|---|---|
| [[s-cohn-2015-coordinated-neuromodulation]] | 離體膜片鉗（[[c-whole-cell-patch-clamp]]）與鈣成像；活體氣味成像；DAN 以 [[e-p2x2]]＋ATP 活化 | 單獨活化 58E02 DAN（與 KC 相隔 > 45 s）：誘發電流約 1.5 → 16 pA（n＝5），ΔF/F0 約 0.7 → 2.5；活體對氣味約 0.15 → 0.53；只活化 γ2 DAN 時小幅下降約 1.4 → 1.1（顯著）；與 KC 配對（< 500 ms）從已增強狀態壓回，約 2.0 → 0.35；活化它本身會改變各格 DAN |
| [[s-handler-2019-dopamine-receptor-timing]] | 離體以乙醯膽鹼刺激 KC、P2X2 活化 PAM，掃描時間差；DopR1、DopR2 剔除；閉迴路同時記錄行為 | 峰值 ΔF/F：逆向（−1.2 s）約 1.22 → 2.8，增強；順向（+0.5 s）約 1.22 → 0.42，減弱；±6 s 幾乎不變；DopR1 剔除後不再減弱、DopR2 剔除後不再增強（見 [[e-dopamine-receptor]]） |

> 數值多為從圖判讀（約），見各來源頁與 [[numbers]]。

## 已知的問題

- **「相隔多久就不再有作用」兩篇不同。** Cohn 相隔 > 45 s 仍讓突觸變強，Handler 相隔 6 s 就幾乎不變，見 [[syn-contradictions]] 1.3。
- **Cohn 的「配對減弱」有起點條件。** 圖 7I 的配對組從已被增強的狀態開始；活體實驗中「只有配對的氣味變弱」這個結果，用的讀數是兩種氣味反應的比值（約 1.35 → 0.6），所以分不出是配對氣味變弱，還是未配對氣味變強。
- **讀法不同不能並排。** Cohn 圖 6A 用電流（pA），其餘與 Handler 用 GCaMP 的 ΔF/F；同一種讀法在不同實驗的起點也不同（Cohn 圖 6B 約 0.7、圖 7C 約 1.5–2）。
- **「推動走開」是引用。** Handler 2019 引 Aso 2014b；庫內沒有來源自己測 γ4 MBON 的行為效果，Cohn 2015 全篇沒有行為讀出。
- **行為不只來自 γ4**（Handler 作者自承），單一 γ4 的變化不能完全代表行為。

## 相關

- 細胞：[[e-mbon]]、[[e-mbon-gamma2alpha1]]、[[e-mbon-gamma5beta2a]]、[[e-dopaminergic-neuron]]
- 工具：[[e-p2x2]]、[[e-r58e02]]、[[e-gcamp]]；製備：[[c-ex-vivo-explant]]
- 概念：[[c-kc-mbon-plasticity]]、[[c-cs-us-timing]]、[[c-mb-compartment]]
- 主題：[[t-timing-rules]]、[[t-dopamine-to-plasticity]]、[[t-mbon-dan-feedback]]
- 來源：[[s-cohn-2015-coordinated-neuromodulation]]、[[s-handler-2019-dopamine-receptor-timing]]
