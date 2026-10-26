---
title: 氣味類化（odor generalization）
created: 2026-10-25
updated: 2026-10-25
tags: [concept, active, mb-learning]
confidence: medium
---

# 氣味類化（odor generalization）

**果蠅學會對某個氣味靠近或躲開之後，對沒受訓、但相似的氣味也出現同樣的反應，叫類化。** 類化越強，記憶越不「專一」。本庫兩篇用它問兩件事：類化從哪裡來（突觸層級的重疊），以及長期記憶是否比短期記憶更不專一。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蘑菇體、KC、葉、區室**：蘑菇體（mushroom body）是果蠅腦中把氣味和好壞經驗連起來的構造；代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」，每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、γ4、α1），細胞以所在區室命名（見 [[e-mushroom-body]]、[[c-mb-compartment]]）。
- **常見詞**：PAM／PPL1＝兩群多巴胺神經元（DAN），分別多傳遞獎賞／懲罰；光遺傳＝讓神經元帶上照光就放電的蛋白（[[e-cschrimson]]）；離體＝把腦取出泡在養液裡，活體＝活果蠅固定後看腦；順向配對＝氣味先、多巴胺後，逆向＝多巴胺先；「未配對」＝兩種刺激錯開、不同時出現；cAMP＝多巴胺受體被活化後在細胞內產生的訊號小分子；※ 推論＝本庫推得、原文沒明說，？待查＝要靠其他資料確認。
- **KC**：Kenyon 細胞，代表氣味；每種氣味只活化一小群，相似氣味活化的 KC 會部分重疊（見 [[e-kenyon-cell]]）。
- **MBON**：蘑菇體輸出神經元（見 [[e-mbon]]）。
- **CS+**：訓練時配了懲罰或獎賞的氣味。
- **STM／LTM**：短期／長期記憶（Ichinose 2015：訓練後 5 分鐘／24 小時）。
- **PI、LI**：行為分數（表現指數、學習指數），見 [[c-performance-index]]。
- **PA、BA、HP、EL、4-MCH、2-MCH**：乙酸戊酯、乙酸丁酯、2-庚酮、乳酸乙酯、4-甲基環己醇、2-甲基環己醇。

## 怎麼算 / 怎麼判定

訓練一個氣味，測驗時改用未訓練的氣味（或與訓練氣味的混合），把那個氣味的分數除以訓練氣味本身的分數，得到「類化比例」。突觸層級則量「配對後，未配對但相似的氣味送到 MBON 的反應被連帶壓低多少」，再與兩氣味的 KC 重疊比例做相關。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-hige-2015-heterosynaptic-plasticity]] | 生理：PA 或 EL 與 PPL1-γ1pedc 活化配對，記錄 MBON-γ1pedc 對四種氣味的反應；行為：以光代替電擊訓練 PA，測 PA、BA、HP 各對 EL | 生理：PA 配對後 BA、HP（與 PA 的 KC 重疊高）被抑制約為 PA 的八成上下，EL 的下降不顯著；重疊與抑制比例的相關 r＝0.90（本庫去掉兩個必然點後重算約 0.85）。行為：PI 約 PA 67、BA 42、HP 38（從圖判讀），即約 PA 的 55–65% |
| [[s-ichinose-2015-reward-recurrent-circuit]] | 4-MCH 配糖；測驗為空氣 vs 4-MCH 與 2-MCH 的不同比例混合，比較 STM 與 LTM | 測驗只有 2-MCH 時，STM 剩約 27%、LTM 剩約 74%（本庫由圖判讀值計算）；作者歸因於訓練後延長的多巴胺釋放（假說，未檢驗） |

> [[s-aso-2016-dan-cell-type-rules]] 圖 3F 把「未受訓的那一對氣味」放進測驗（接近 0），用來**排除**類化對「記住兩組配對」的解釋；它沒有量類化本身，故不列入表。數值見 [[numbers]]。

## 引用時的陷阱

1. **Hige 2015 的生理與行為是不同果蠅、不同光協定**（生理 1 ms × 1，行為 500 ms × 12）；「類化由突觸干擾介導」是對應，沒有「阻斷這個減弱就消除類化」的因果實驗。
2. **r＝0.90 有兩點是定義上必然的**（CS+ 與自己的重疊為 1）；剩下六點分成兩群，較像高重疊對低重疊的兩組比較。
3. **Ichinose 2015 沒有檢定兩條曲線的斜率差**（只有單因子 ANOVA），而且 LTM 的起點本來就低（約 0.31 vs 0.56）；該實驗的 LI 算法也與其他圖不同，不宜跨圖比大小。
4. **兩篇的機制不同**：Hige 2015 是 KC 重疊（有生理資料），Ichinose 2015 是「延長的多巴胺作用在沒對 CS+ 反應的 KC 上」（假說）；後者需要多巴胺在 KC 沒有活動時也能改變突觸，與「KC 正在活動、同時多巴胺到達，突觸才會改變」這個前提（[[c-coincidence-detection]]）有張力（原文用 may，見 [[s-ichinose-2015-reward-recurrent-circuit]] 第五節）。
5. **行為的類化比突觸層級弱**（Hige 2015：約 55–65% 對約八成）；※ 推論：突觸記錄只量了 γ1pedc 一格，而行為由多個區室合成，其他格的類化可能較弱，拉低了行為上的比例。

## 相關

- 概念：[[c-kc-mbon-plasticity]]、[[c-coincidence-detection]]、[[c-memory-consolidation]]、[[c-performance-index]]
- 實體：[[e-kenyon-cell]]、[[e-mbon-gamma1pedc]]、[[e-ppl1-gamma1pedc]]、[[e-pam-alpha1]]
- 主題：[[t-dopamine-to-plasticity]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-aso-2016-dan-cell-type-rules]]
