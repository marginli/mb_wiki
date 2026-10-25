---
title: Epac 系 cAMP 感測器（Epac-based cAMP sensor）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-learning]
confidence: medium
---

# Epac 系 cAMP 感測器（Epac-based cAMP sensor）

## 是什麼

一種用基因工程讓神經元自己製造、會隨 cAMP 濃度改變螢光顏色比例的蛋白質。cAMP（環腺苷酸）是細胞內的「第二傳訊者」：多巴胺受體被活化後，細胞內的 cAMP 會升高，再啟動下游的改變（見 [[c-camp-signaling]]）。有了這個感測器，就能在顯微鏡下看到 [[e-kenyon-cell]] 軸突裡 cAMP 的起落。

**原理：FRET。** 感測器兩端各接一個螢光蛋白，青色（CFP）與黃色（YFP），中間夾一段會抓 cAMP 的片段。兩者靠得近時，CFP 吸收的能量轉給 YFP（螢光共振能量轉移，Förster resonance energy transfer, FRET），黃光多、青光少；cAMP 結合後兩者分開，青光相對黃光上升。所以讀數是 CFP/YFP 的比值變化，寫成 ΔR/R0 或 ΔR/R（比值相對基線變化了多少）。

## 版本與規模

| 來源 | 論文中的名稱 | 出處 | 版本關係 |
|---|---|---|---|
| Tomchik 2009 | Epac1-camps（UAS-epac1-camps） | 引 Nikolaev et al. 2004（原始感測器）與 Shafer et al. 2008（已用於果蠅）；致謝中說果蠅品系由 Paul Taghert 提供 | 明說 |
| Handler 2019 | UAS-EPAC（cAMP） | 試劑表的來源欄寫 Shafer et al. 2008 | 是不是 Epac1-camps，論文沒有明說 |

※ 推論：Handler 2019 的 UAS-EPAC 很可能就是 Epac1-camps，或至少是同一來源的品系。依據：兩篇都把它的出處引到 Shafer et al. 2008，而 Tomchik 的品系提供者 Taghert 也是 Shafer 2008 的作者之一。不確定之處：同一篇文獻可能做了不止一種品系或插入位置，Handler 沒寫感測器全名：？待查。

## 庫內誰用了它

| 來源 | 表現在哪裡（驅動品系） | 成像方式 | 讀法 | 用它算出什麼 |
|---|---|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | KC：238Y、c739（這一組同時改用另一個感測器轉基因品系，插在第 3 號染色體，用來排除插入位置造成的假象）、c305a、1471；另有 DPM 神經元（c316）、投射神經元（GH146） | 離體腦，共軛焦顯微鏡 | 「反 FRET 比」（CFP 放分子、YFP 放分母，cAMP 升高時比值上升）的變化 ΔR/R0，以百分比表示 | 多巴胺、章魚胺（昆蟲腦中類似腎上腺素的物質）的劑量反應；乙醯膽鹼與多巴胺配對時的協同（配對比兩者單獨相加還大）及其時間窗 |
| [[s-handler-2019-dopamine-receptor-timing]] | KC：OK107-Gal4；在 γ4/γ5 區室量軸突 | 離體腦，雙光子，激發波長 850 nm（其他感測器用 920 nm） | DAN 活化後 4 s 內的 CFP/YFP 比平均，除以刺激前 2–4 s 的比值，寫成 ΔR/R（小數） | 不同時間差（ISI）下的 cAMP；DopR1、DopR2 突變後 cAMP 的變化 |

**Tomchik 2009 的驗證**：用 forskolin（直接活化製造 cAMP 的酵素）確認感測器有濃度依賴的反應，最高可達約 40%（從圖判讀，見 [[numbers]]），而多巴胺即使加到最高劑量（10 mM），ΔR/R0 也只升到約 12%（見 [[numbers]]），可見多巴胺停在約 12% 不是感測器到頂；若 YFP 自己因褪色等原因變暗，CFP/YFP 比值也會上升、像是 cAMP 升高；作者用 514 nm 的光只激發 YFP，看到 YFP 沒有變暗，排除了這種假訊號；另一種結構相近的訊號分子 cGMP 也可能讓感測器反應，這項干擾的檢查在補充圖 2：？待查。Handler 2019 的正文與方法沒有提到這類驗證（已搜 forskolin、validat、bleach；補充圖未取得，裡面有沒有：？待查），作者在討論中自陳感測器的靈敏度與動態範圍有限。

**2015–2018 新收的五篇（Cohn、Ichinose、Aso、Felsenberg 2017、2018）都沒有用 cAMP 感測器**（全文 grep `epac` 無結果）。

## 已知的問題

- **兩篇的 cAMP 結論不同，本頁不裁決。** Tomchik：只有乙醯膽鹼在前、多巴胺在後才出現協同，倒過來沒有。Handler：順向、逆向都產生 cAMP，同時發生最多，因此 cAMP「分不出先後」。見 [[syn-contradictions]] 1.2 與 [[c-coincidence-detection]]。
- **數值不能跨篇比較。** Tomchik 以百分比、共軛焦、浴灌或噴藥；Handler 以小數、雙光子、離子導入與 P2X2 活化 DAN；讀取的時間窗也不同。同一篇裡，Tomchik 也提醒不同驅動品系的表現量不同，跨品系比絕對幅度只能當參考。
- **Tomchik 的「協同」靠的是「配對 vs 單獨相加」，Handler 沒有做這個比較**，只比不同時間差下的 cAMP 大小。兩篇對「同時性偵測」的操作定義不同。

## 相關

- 概念：[[c-camp-signaling]]、[[c-coincidence-detection]]、[[c-cs-us-timing]]
- 細胞：[[e-kenyon-cell]]；其他感測器：[[e-gcamp]]
- 主題：[[t-dopamine-to-plasticity]]、[[t-timing-rules]]；矛盾：[[syn-contradictions]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-handler-2019-dopamine-receptor-timing]]
