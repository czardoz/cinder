#ifndef __STRICTM_MODULE_OBJ_H__
#define __STRICTM_MODULE_OBJ_H__
#include <string>
#include "StrictModules/Objects/instance.h"

namespace strictmod::objects {
class StrictModuleObject : public StrictInstance {
 private:
  std::string name_;

 public:
  StrictModuleObject(
      std::shared_ptr<StrictType> type,
      std::string name,
      std::shared_ptr<DictType> dict = nullptr);

  virtual std::string getDisplayName() const override;

  const std::string getModuleName() const {
    return name_;
  }

  static std::shared_ptr<StrictModuleObject> makeStrictModule(
      std::shared_ptr<StrictType> type,
      std::string name,
      std::shared_ptr<DictType> dict = nullptr);
};
} // namespace strictmod::objects
#endif // !__STRICTM_MODULE_OBJ_H__