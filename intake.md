# 收錄登記簿

`papers/` 底下每一份 PDF 的處理狀態。**新論文丟進 `papers/` 之後，這裡是唯一需要人／Claude 手動維護的紀錄。**

其餘的都能從檔案系統推出來，所以這份登記簿只記三件推不出來的事：

1. **哪些 PDF 決定不收錄，以及為什麼**——沒有這一條，每次更新都會重新提議同一份被否決的檔案。
2. **每一份屬於哪個領域**——決定它進 `index.md` 的哪一個 H2。
3. **處理日期與備註**。

「涉及哪些主題」**不記在這裡**，因為它已經在該來源頁的「相關」段與 `index.md` 裡了；
記第三次只會多一個會走鐘的地方。

## 對帳

登記簿會失準，所以不要只信它。查核用：

```bash
python3 tools/scan.py          # 完整報告：待處理／已收錄／不收錄／異常
python3 tools/scan.py --todo   # 只印待處理的檔名，一行一個
```

腳本比對三個來源：`papers/` 實際存在的 PDF、`wiki/sources/*.md` 的 `citation` 欄指向的 PDF、
以及本檔的表格。三者不一致就報異常，**但不自動修正**——修正要判斷，交給人。

三者都以檔名為鍵，因此**同一篇論文換個檔名再丟進來，對帳會把它當成全新的一篇**。
`scan.py` 為此另跑一輪不看檔名的重複偵測：**sha256／DOI／PDF 內嵌標題／逐頁詞組指紋**四道任一成立
即列為異常，另有逐頁重疊 50–80% 與首頁相似度兩個提示。
判定為重複時：狀態填 `不收錄`、備註寫「與 `<原檔名>` 同一篇」，並在下面的判定紀錄補一段。

**判定不收錄之後，那份檔從 `papers/` 消失是預期的收斂結果，`scan.py` 不算它異常**（登記列與判定紀錄留著，下次同一份再丟進來照樣被攔）。
但 `已收錄`／`待處理`／`處理中` 的檔案消失**仍然是異常**——尤其 `已收錄`，那表示某個來源頁的 `citation` 指向一個開不起來的 PDF。

## 狀態的四種值

| 狀態 | 意思 |
|---|---|
| `已收錄` | 來源頁已寫完，且相關主題／概念／實體頁已更新 |
| `待處理` | 已放進 `papers/`，還沒動 |
| `處理中` | 正在寫，尚未完成。**中斷時務必留下這個狀態**，否則下次會被當成待處理重做 |
| `不收錄` | 已判定不收。**必須在備註欄寫出理由**，否則下次會被重新提議 |

## 登記表

| PDF 檔名 | 狀態 | 來源頁 | 領域 | 日期 | 備註 |
|---|---|---|---|---|---|
| `2009-Dynamics of learning-related cAMP signaling and stimulus integration in the Drosophila olfactory pathway.pdf` | 已收錄 | [[s-tomchik-2009-camp-dynamics]] | 學習的訊號機制 | 2026-10-25 | NIH PMC 作者稿（PMC4080329），© Elsevier。**補充資料未取得**：補充方法與補充圖 2、3、5、8，需人工從 https://pmc.ncbi.nlm.nih.gov/articles/PMC4080329/ 下載（自動下載被反機器人驗證擋下） |
| `2015-Heterosynaptic Plasticity Underlies Aversive Olfactory Learning in Drosophila.pdf` | 已收錄 | [[s-hige-2015-heterosynaptic-plasticity]] | 學習的訊號機制 | 2026-10-25 | 出版社排版版，© Elsevier。**補充資料未取得**：補充方法與圖 S1–S7（含 P.I. 公式、LTD 持續時間圖 S4），需人工從 https://pmc.ncbi.nlm.nih.gov/articles/PMC4674068/ 下載 |
| `2019-Distinct dopamine receptor pathways underlie the temporal sensitivity of associative learning.pdf` | 已收錄 | [[s-handler-2019-dopamine-receptor-timing]] | 學習的訊號機制 | 2026-10-25 | HHS PMC 作者稿（PMC9012144），© Elsevier，含 STAR Methods。**補充圖 S1–S8 未取得**，需人工從 https://pmc.ncbi.nlm.nih.gov/articles/PMC9012144/ 下載 |
| `2015-Coordinated and compartmentalized neuromodulation shapes sensory processing in Drosophila.pdf` | 已收錄 | [[s-cohn-2015-coordinated-neuromodulation]] | 學習的訊號機制；記憶寫入之後 | 2026-10-25 | HHS PMC 作者稿（PMC4732734），© Elsevier。**補充資料 S1–S7 與表 S1 未取得**（含 ATP 刺激參數，見 syn-contradictions 1.3），需人工從 https://pmc.ncbi.nlm.nih.gov/articles/PMC4732734/ 下載 |
| `2015-Reward signal in a recurrent circuit drives appetitive long-term memory formation.pdf` | 已收錄 | [[s-ichinose-2015-reward-recurrent-circuit]] | 記憶寫入之後 | 2026-10-25 | *eLife*，CC BY（PMC4643015）。PDF 依規則仍不進 git。**figure supplement 與影片 1 未取得**，見 https://elifesciences.org/articles/10719 |
| `2016-Dopaminergic neurons write and update memories with cell-type-specific rules.pdf` | 已收錄 | [[s-aso-2016-dan-cell-type-rules]] | 記憶寫入之後；學習的訊號機制 | 2026-10-25 | *eLife*，CC BY（PMC4987137）。PDF 依規則仍不進 git。**figure supplement（含其他區室的時間差曲線）與影片未取得**，見 https://elifesciences.org/articles/16135 |
| `2017-Re-evaluation of learned information in Drosophila.pdf` | 已收錄 | [[s-felsenberg-2017-re-evaluation]] | 記憶寫入之後 | 2026-10-25 | 出版社版，© Springer Nature；免費全文為 Europe PMC 作者稿（PMC5392358）。PDF 含方法與延伸圖 1–6；**Supplementary Information 與 Source Data 未取得** |
| `2018-Integration of parallel opposing memories underlies memory extinction.pdf` | 已收錄 | [[s-felsenberg-2018-memory-extinction]] | 記憶寫入之後 | 2026-10-25 | *Cell*，CC BY 4.0（PMC6198041）。PDF 依規則仍不進 git。含補充圖 S1–S7；**表 S1（全部 n 與 p 值）未取得**，需人工從 https://pmc.ncbi.nlm.nih.gov/articles/PMC6198041/ 下載 |

## 不收錄的判定紀錄

目前無。
