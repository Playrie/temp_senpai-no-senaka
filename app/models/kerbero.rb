class Kerbero < ApplicationRecord
    validates :common_password, length: {minimum: 6, maximum: 128}

    def sex
        case self.sex_num
        when 0
            return "雄"
        when 1
            return "雌"
        else
            return ""
        end
    end
end
