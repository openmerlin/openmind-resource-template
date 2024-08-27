# changelog同步逻辑说明

## changelog同步

定时任务于每日凌晨1点执行，读取CHANGELOG_ZH.md和CHANGELOG_EN.md的文件内容，写入merlin-server数据库。

## changelog版本更新消息通知

同样在上述定时任务中，执行完文件内容同步后，检查CHANGELOG_ZH.md的最新commit message，匹配正则表达式^release_update_(v\d+(.\d+)+)$，且该commit于24小时内提交（对应定时脚本执行频率，避免重复发送）。

之后会用匹配到的版本vx.x.x号向全部用户发送版本更新消息通知。

因此，更新changelog时，如果不发送消息通知，commit message可随意填写。如需要发送通知，CHANGELOG_ZH.md文件的commit message需严格按照release_update_v1.1.1的格式填写。
